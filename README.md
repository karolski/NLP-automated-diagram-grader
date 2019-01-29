# marbel
Research project at Maastricht University
The notebooks serve to asses the correctness of causal relationship students indicate after reading a text. Their correctness is assesed throuhg comparison and matching of student's responses with the model response for each text. The notebooks use Latent Semantic Analysis methods, with the basic analysis involving comparison of weighted word embeddings through word2vec model. 

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
1. Open the terminal enter the repository
2. Run jupyter application
```
$ jupyter notebook 
```
...- your browser will open a new tab with jupyter interface. You'll see the contents of the repository folder

3. Open a notebook **A_measure_sentence_similarity.ipynb**

...- the kernel for this project is **Python3_marble** choose it in the top menu **kernel>Change kernel>Python3_marble**.

4. Edit and run the cells. Your results will be saved in .csv files in the main directory of the repository. Every time you run the notebooks, new results will overwrite the previous ones. If you want to save the results, rename them or copy to another folder.


## Notebooks sequence
A.  **A_measure_sentence_similarity.ipynb**
1. I take “Example_dataset_marble_v2 - 2_data_no_omission.csv” – the dataset you gave at the very beginning, with English translations by Google-translate.
2. I take “correct_answers.csv” – the correct answers for each task in the dataset
3. I calculate the difference between what student wrote in a given field and all sentences from the model (using average cosinus distance 4. between words embedded using word2vec embeddings).
5. I choose the sentence from the model, that seems the most similar to what students wrote.
6. I save the student sentences with their “matches” from the model in “avg_wv2_matched.csv”
Based on the matches I reconstruct the logical order of the sentences (taking under consideration only the sentences that match well enough with some sentence from the model, let’s say more than 0.2, otherwise I treat them as omissions). The logical order takes a form of e.g. “1324”, meaning: The student put the sentence 1, than 3, than 2, than 4. The model is “1234”
7. I measure how different the logical order of the student is from the logical order of the model (using Levenshtein distance)
8. I put the logical orders of the students’ sentences in a table.
9. I take “self_assesment.csv” – the relevant columns from the last file you sent me,
10. I make a joined table of self assessment and logical orders of sentences
11. I save the detected order together with the its score and sum of semantic similarity-to-model points in “logical_order_score_similarity>0.2.csv”*
12. I measure Pearson correlation of logical-order-score and similarity-to-model-sentences-score to self assessment
13. I save the correlations in “correlations_similarity>0.2.csv”*
 
*0.2 in the filename refers to the MIN_THRESHOLD_OF_SIMILARITY = 0.2 that I assume to treat a sentence of a student as one of the sentence from the model.If the sentence student wrote is not similar enough to any sentence in the model, the sentence is treated as an omission.

## Tips for dummies
- get the texts from any language translated in google spreadsheets using `GOOGLETRANSLATE` function:
![alt text](https://raw.githubusercontent.com/karolski/marbel/master/translate_in_gspreadsheet.png)

- get the files from .sav format to .csv on https://pspp.benpfaff.org/


## Notes

- [WordNet Similarity online demo](ws4jdemo.appspot.com) good for getting a feel for the different algorithms provided by WordNet. uses [this java library] (https://code.google.com/archive/p/ws4j/)

- The specific algorithms at present are the following: 
- string matching method based on keywords and syntatic structure [paper](https://www.hindawi.com/journals/mpe/2015/203475/#B6), the 
- TF-IDF method based on freqiencies [wikipedia article](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), 


### Tools: hosting the jupiter notebooks for free: 
- Google's colab - https://colab.research.google.com/drive/1Br0ccGZ-CW1sCOd1uyIo6IpOdOTIMnhj#scrollTo=H1-7m5zZoF_1
- Azure - https://research-anonhzhyfg.notebooks.azure.com/j/notebooks/notebook1.ipynb
- Nbvirert - https://nbviewer.jupyter.org/
- Mybinder - https://hub.mybinder.org/user/jvns-pandas-cookbook-hofdfcpb/tree

Thoughts
- it seems to me that keyword analysis would be enough as some of the answers of the students are mental shortcuts, where they indicate what they think is the cause in keywords, counting on the examiner understanding them. They can use keywords, because the context of their answers and their linguistic function are known, based on the questions. Hence the keywords detection algorithm should also be able to make use of question and example answers, or the text as a context that will make determining concepts behind the words more accurate, and thus increasing the accuracy of the assessment.


## To Read
- https://arxiv.org/pdf/1802.05667.pdf
- http://searchivarius.org/blog/brief-overview-querysentence-similarity-functions
- https://www.irjet.net/archives/V4/i1/IRJET-V4I129.pdf
- http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.210.9942&rep=rep1&type=pdf

## Bibliography

<li>
    <a href="https://www.hindawi.com/journals/mpe/2015/203475/">
        Calculation of Sentence Semantic Similarity Based on Syntactic Structure
Xiao Li1 and Qingsheng Li1,2
    </a> - Super cool article about merging analysis of sentence structure  with the analysis of meaning in terms of Wordnet-like models
</li>
<li>
    <a href="http://nlp.town/blog/sentence-similarity/">
        Comparing Sentence Similarity Methods
    </a> - Amazing comparison + summary with Jupyter notebook reference included
</li>    

<li>
    <a href="https://github.com/nlptown/nlp-notebooks">
    cross lingual embedding repo
    </a> - same guy as above
</li>    
<li> 
https://nlp.stanford.edu/projects/glove/ - source of GloVe dataset
</li>
<li>
https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf - word2vec paper
</li>
<li>
 - 
</li>
## Bibliography about alternative aproaches:

- Alternative language representation: [WordNet](https://wordnet.princeton.edu/) from Princeton University
- gui application: [SEMILAR](http://www.semanticsimilarity.org/) SEMILAR API comes with various similarity methods based on Wordnet, Latent Semantic Analysis (LSA), Latent Dirichlet Allocation (LDA), BLEU, Meteor, Pointwise Mutual Information (PMI), Dependency based methods, optimized methods based on Quadratic Assignment, etc. 
- API serveice [cortical.io](https://www.cortical.io/compare-text.html) with similar method
- n-gram vectors - pick a value of n (say, 3), and hash every 3-word sequence in the phrase into a vector. Normalize the vector to unit length, then take the dot product of different vectors to detect similarity.
J. Mitchell and M. Lapata, “Composition in Distributional Models of Semantics,” Cognitive Science, vol. 34, no. 8, pp. 1388–1429, Nov. 2010., DOI 10.1111/j.1551-6709.2010.01106.x

## Bibliography about methods I used:

- Word Mover Distance [paper](http://mkusner.github.io/publications/WMD.pdf)
- explanation of Mikolov's word2vec obejctive function and learning rates [paper](https://arxiv.org/pdf/1411.2738.pdf)

## Bibiliography on metacognitive monitoring, effects of practice testing on learning and intervention with online tools:


Thiede, K. W., Anderson, M. C. M., & Therriault, D. (2003). Accuracy of metacognitive monitoring affects learning of texts. Journal of Educational Psychology, 95, 66-73

De Bruin, A.B.H., Dunlosky, J., & Cavalcanti. R.B. (2017). Monitoring and regulation of learning in medical education: The need for predictive cues. Medical Education, 51, 575-58

Van Loon, M.H., De Bruin, A.B.H., Van Gog, T., & Van Merriënboer, J.J.G., & Dunlosky, J. (2014). Can students evaluate their understanding of cause-and-effect relations? The effects of diagram completion on monitoring accuracy. Acta Psychologica, 151, 143-154.
 
De Bruin, A.B.H, Kok, E.M., Lobbestael, J., & de Grip, A. (2017). The impact of an online tool for monitoring and regulating learning at university: overconfidence, learning strategy, and personality. Metacognition and Learning, 12, 21-43.
 
De Bruin, A.B.H, & van Merriënboer, J.J. (2017). Bridging Cognitive Load and Self-Regulated Learning Research: A complementary approach to contemporary issues in educational research. Learning and Instruction, 51, 1-9.

## Go further:
[Googles state-of-art (30.02.2019) free Natural Language processing tool "Bert" in jupyter notebook.]
(https://colab.research.google.com/github/tensorflow/tpu/blob/master/tools/colab/bert_finetuning_with_cloud_tpus.ipynb#scrollTo=uu2dQ_TId-uH)

[Y. Li, D. McLean, Z. A. Bandar, J. D. O'Shea and K. Crockett, "Sentence similarity based on semantic nets and corpus statistics," in IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 8, pp. 1138-1150, Aug. 2006.](https://www.researchgate.net/publication/232645326_Sentence_Similarity_Based_on_Semantic_Nets_and_Corpus_Statistics)[code](https://github.com/chanddu/Sentence-similarity-based-on-Semantic-nets-and-Corpus-Statistics-)



