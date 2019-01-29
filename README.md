# marble
Marble is a series of Research projects at Maastricht University. This project is concerned with proof-of-concept application of Sentence Similarity Measures to research on self-monitoring in learning and the influence of practice testing on learning efficacy. 
The notebooks serve to asses the correctness of causal relationships students indicate after reading a text. Their responses are compared and matched with the phrases from the model response for each text. The basic analysis involves comparison of weighted average of embeddings of words embedded with a pretrained Word2vec model. The comparison methods include regular cosine distance, Smooth Inverse Frequency, Word Mover's Distance, each with or without weighitng the words by frequency of occurance in traing sets. Analysis can be extended by use of Infersent and Google Sentence Encoder - alternative and more sophisticated sentence encoders. The comparison of causal sequences is done with Levenshtein distance, treating each sentence as a character. More detailed information about analysis can be found within the notebooks themsleves.

## Requirements
- Unix based system (tested on Ubuntu and MacOS)
- [Python](https://www.python.org/downloads/) >= 3.4, recommended 3.6
- [pip](https://pip.pypa.io/en/stable/installing/) python package manager usually installed with python >= 3.4
- [virtualenv](https://virtualenv.pypa.io/en/stable/installation/ ) - tool for creating isolated python environments. You can install it using a command ```$ pip3 install virtualenv ```
- Jupyter notebook - application for interactive development. You can install it with ```$ pip3 install jupyter```

## Installation for the first time
The scripts can be run and edited in a virtual environment with all the dependencies within installed within it.
1. Clonse the repository and enter its directory:
``` 
$ git clone https://github.com/karolski/marbel.git 
$ cd marbel
```
2. Create a virtual environment
```
$ ./01create_virtualenv
```
3. Install all required dependencies and download the models
```
$ ./02install_dependencies
$ ./03_download_w2v_model
```

## Run and edit the notebooks
1. Open the terminal enter the repository. *Tip for dummies: [this cheatsheet](https://www.git-tower.com/blog/command-line-cheat-sheet/) will help you navigat within the terminal*
2. Run jupyter application
```
$ jupyter notebook 
```
  - your browser will open a new tab with jupyter interface. You'll see the contents of the repository folder

3. Open a notebook **A_measure_sentence_similarity.ipynb**

 - the kernel for this project is **Python3_marble** choose it in the top menu **kernel>Change kernel>Python3_marble**.

4. Run or edit the cells. You run them with "play" button. You can run the whole notebook by pressing [ <img height="20" src=https://cdn4.iconfinder.com/data/icons/defaulticon/icons/png/256x256/media-fast-forward.png> ]  Your results will be saved in .csv files in the main directory of the repository. Every time you run the notebooks, new results will overwrite the previous ones. If you want to save the results, rename them or copy to another folder.

5. Open a notebook **B_Postprocessing-measure_distance.ipynb**, and run (or edit) the cells.


## Notebooks sequence
The logic of the cells is outlined in the notebooks themselves. Here is the general overview of the actions within the notebooks.

**A_measure_sentence_similarity.ipynb**
1. Take “Example_dataset_marble_v2 - 2_data_no_omission.csv” or other file specified as INPUT_FILE – the input dataset containig responses of students, with their English translations.
2. Take “correct_answers.csv” – the correct answers for each task in the dataset as model answers
3. Calculate the difference between what student wrote in a given field and all sentences from the model using cosinus distance between sentence embeddings.
4. Choose the sentence from the model, that seems the most similar to what students wrote and match them.
5. Save overall result, and the result of a specfic algorithm - by default embedding sentences by averaging the word embeddings with ommission of stopwords such as "the" "just" etc. The result of will be saved under “avg_wv2_matched.csv” (or another filename specified).

**B_Postprocessing-measure_distance.ipynb**

6. Discard the sentences that do not match any sentence from the model well enough
7. Based on the matches reconstruct the logical order of the sentences. The logical order takes a form of e.g. “1324”, meaning: The student put the sentence 1, than 3, than 2, than 4. The model is “1234”
8. I measure how different the logical order of the student is from the logical order of the model (using [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance))
9. I take “self_assesment.csv” – the table with self assesment of students, and "Result_per_stud.csv" - the table with students assesment by the observer.
10. I make a joined table of self assessment, observer assesment, accuracy scores and logical orders of sentences, accuracy
11. I save the detected order together with the its score and sum of semantic similarity-to-model points in “AVG_W2V_logical_order_score_similarity>0.2.csv”*
12. I measure Pearson correlation of logical-order-score and similarity-to-model-score, accuracy-score, observer-score to self assessment
13. I save the correlations in “AVG_W2V_correlations_similarity>0.2.csv”* and "AVG_W2V_all_correlations.csv"
 
*0.2 in the filename refers to the MIN_THRESHOLD_OF_SIMILARITY = 0.2 that I assume to treat a sentence of a student as one of the sentence from the model.If the sentence student wrote is not similar enough to any sentence in the model, the sentence is treated as an omission.

*All filenames are explicitelly defined in the notebooks and can be changed

## Extra possiblities
- use **GloveINfersentGoogle_experiment.ipynb** to see the models above applied to your dataset the same way word2vec was. Theoutput files look exactly like the ones from notebook basic A_... notebook, and you can apply postprocessing on them
- use **W2V_on_SICK_data.ipynb** to see and graph how the method used in the experiment performs on SICK and STS benchmark datasets.
- use **GloveINfersentGoogle_onSICK_data.ipynb** to see how more advances sentence encoders perform on SICK benchmark dataset. You will need to download more models and extra libraries. The instruction will be found inside the notebook.


## Tips for preparing the input files

- get the texts from any language translated in google spreadsheets using `GOOGLETRANSLATE` function:

![alt text](https://raw.githubusercontent.com/karolski/marbel/master/translate_in_gspreadsheet.png)

- get the files from .sav format to .csv on https://pspp.benpfaff.org/

### Tools: hosting the jupiter notebooks for free: 
- Google's colab - https://colab.research.google.com/notebooks/welcome.ipynb#recent=true
- Azure - https://notebooks.azure.com/#
- Mybinder - https://mybinder.org/

## Bibliography about methods I used:
- Article about the repository used as a codebase [article](http://nlp.town/blog/sentence-similarity/). It compares different sentence similarity measures
- Word Mover Distance [paper](http://mkusner.github.io/publications/WMD.pdf)
- explanation of Mikolov's word2vec obejctive function and learning rates [paper](https://arxiv.org/pdf/1411.2738.pdf)
- Word2vec original [paper](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)
- original Glove dataset and references [link](https://nlp.stanford.edu/projects/glove/)

## Bibliography about alternative aproaches:

- Alternative language representation: [WordNet](https://wordnet.princeton.edu/) from Princeton University
- gui application: [SEMILAR](http://www.semanticsimilarity.org/) SEMILAR API comes with various similarity methods based on Wordnet, Latent Semantic Analysis (LSA), Latent Dirichlet Allocation (LDA), BLEU, Meteor, Pointwise Mutual Information (PMI), Dependency based methods, optimized methods based on Quadratic Assignment, etc. 
- API serveice [cortical.io](https://www.cortical.io/compare-text.html) with similar method
- n-gram vectors - pick a value of n (say, 3), and hash every 3-word sequence in the phrase into a vector. Normalize the vector to unit length, then take the dot product of different vectors to detect similarity.
J. Mitchell and M. Lapata, “Composition in Distributional Models of Semantics,” Cognitive Science, vol. 34, no. 8, pp. 1388–1429, Nov. 2010., DOI 10.1111/j.1551-6709.2010.01106.x
- string matching method based on keywords and syntatic structure [paper](https://www.hindawi.com/journals/mpe/2015/203475/#B6), the 
- Calculation of Sentence Semantic Similarity Based on Syntactic Structure
Xiao Li1 and Qingsheng [paper](https://www.hindawi.com/journals/mpe/2015/203475/) - article about merging analysis of sentence structure  with the analysis of meaning in terms of Wordnet-like models
- Kazi, Hameedullah & Haddawy, Peter & Suebnukarn, Siriwan. (2012). Employing UMLS for generating hints in a tutoring system for medical problem-based learning. Journal of biomedical informatics. 45. 557-65. [link](https://www.researchgate.net/publication/221722664_Employing_UMLS_for_generating_hints_in_a_tutoring_system_for_medical_problem-based_learning) *employeeing a predefined ontology systems to produce easily verifiable tasks with a precise hinting system*


## Bibiliography on metacognitive monitoring, effects of practice testing on learning and intervention with online tools:


Thiede, K. W., Anderson, M. C. M., & Therriault, D. (2003). Accuracy of metacognitive monitoring affects learning of texts. Journal of Educational Psychology, 95, 66-73

De Bruin, A.B.H., Dunlosky, J., & Cavalcanti. R.B. (2017). Monitoring and regulation of learning in medical education: The need for predictive cues. Medical Education, 51, 575-58

Van Loon, M.H., De Bruin, A.B.H., Van Gog, T., & Van Merriënboer, J.J.G., & Dunlosky, J. (2014). Can students evaluate their understanding of cause-and-effect relations? The effects of diagram completion on monitoring accuracy. Acta Psychologica, 151, 143-154.
 
De Bruin, A.B.H, Kok, E.M., Lobbestael, J., & de Grip, A. (2017). The impact of an online tool for monitoring and regulating learning at university: overconfidence, learning strategy, and personality. Metacognition and Learning, 12, 21-43.
 
De Bruin, A.B.H, & van Merriënboer, J.J. (2017). Bridging Cognitive Load and Self-Regulated Learning Research: A complementary approach to contemporary issues in educational research. Learning and Instruction, 51, 1-9.

## Go further:
Googles state-of-art (30.02.2019) free Natural Language processing tool "Bert" in jupyter notebook.[link](https://colab.research.google.com/github/tensorflow/tpu/blob/master/tools/colab/bert_finetuning_with_cloud_tpus.ipynb#scrollTo=uu2dQ_TId-uH)

Y. Li, D. McLean, Z. A. Bandar, J. D. O'Shea and K. Crockett, "Sentence similarity based on semantic nets and corpus statistics," in IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 8, pp. 1138-1150, Aug. 2006.[link](https://www.researchgate.net/publication/232645326_Sentence_Similarity_Based_on_Semantic_Nets_and_Corpus_Statistics)[code](https://github.com/chanddu/Sentence-similarity-based-on-Semantic-nets-and-Corpus-Statistics-)

cross lingual embeddings [respository](https://github.com/nlptown/nlp-notebooks) by @nlptown 

Kazi, H., Haddawy, P., & Suebnukarn, S. (n.d.). Expanding the Plausible Solution Space for Robustness in an Intelligent Tutoring System. Intelligent Tutoring Systems, 583-592. - [article about intelligent tutoring systems](https://pdfs.semanticscholar.org/63d1/64392c3c2200c30fc0f4cc3aefbe3378a952.pdf)

## Notes

- [WordNet Similarity online demo](ws4jdemo.appspot.com) good for getting a feel for the different algorithms provided by WordNet. uses [this java library](https://code.google.com/archive/p/ws4j/)
- it seems to me that keyword analysis would be enough as some of the answers of the students are mental shortcuts, where they indicate what they think is the cause in keywords, counting on the examiner understanding them. They can use keywords, because the context of their answers and their linguistic function are known, based on the questions. Hence the keywords detection algorithm should also be able to make use of question and example answers, or the text as a context that will make determining concepts behind the words more accurate, and thus increasing the accuracy of the assessment.
- TF-IDF method based on freqiencies [wikipedia article](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), 
