# marbel
Research project at maastricht university

# Requirements
Python 3.4+, recommended 3.6 with pip installed 
- Unix based system (tested on Ubuntu and MacOS)
- Jupyter notebook

# Installation for the first time
The scripts can be run and edited in a virtual environment with all the dependencies within installed within it.
1. Create a virtual environment
2. Activate it
3. Install all required dependencies
4. Put the input csv Files in 

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


## Notes

- WordNet Similarity for Java online demo was helpful in getting a feel for the different algorithms provided by WordNet: ws4jdemo.appspot.com 
- check out this paper: Sentence similarity based on semantic nets and corpus statistics (PDF)
- check into the WordNet project at Princeton University.
- I would suggest taking a look at SEMILAR - http://www.semanticsimilarity.org/ 
- cortical.io has developed a process for calculating the semantic similarity of two expressions and they have a demo of it up on their website. They offer a free API providing access to the functionality,
- Take a look at http://mkusner.github.io/publications/WMD.pdf 
- Update : I found this library very useful for measuring similarity between two words. Also the ConceptNet similarity mechanism is very good.
- and this library for measuring semantic similarity between sentences
- The best package I've seen for this is Gensim, found at the Gensim Homepage.
- hard problem. The closest task that I know about is paraphrase detection, where you want to determine if two sentences semantically entail each other. aclweb.org/aclwiki/… 
- The Google Sentence Encoder is Google’s answer to Facebook’s InferSent.
- The specific algorithms at present are the following: string matching method based on keywords [6], the TF-IDF method based on vector space model [7], the calculation method of sentence similarity based on semantic dictionary [3], the calculation method of sentence similarity based on dependency analysis [8], and so on.
- UMBC Semantic Similarity Service 
- from the description on their website, it can do the following things
    - Top-N Similarity -- Gives top-n most similar words to an input word
    - Phrase Similarity -- Computes semantic similarity between two short noun or verb phrases.
    - STS Similarity -- Computes Semantic Textual Similarity between two sentences or phrases.


Tools: hosting the jupiter notebooks for free: 
- https://research-anonhzhyfg.notebooks.azure.com/j/notebooks/notebook1.ipynb
- https://nbviewer.jupyter.org/
- https://hub.mybinder.org/user/jvns-pandas-cookbook-hofdfcpb/tree
- https://colab.research.google.com/drive/1Br0ccGZ-CW1sCOd1uyIo6IpOdOTIMnhj#scrollTo=H1-7m5zZoF_1


SEMILAR API comes with various similarity methods based on Wordnet, Latent Semantic Analysis (LSA), Latent Dirichlet Allocation (LDA), BLEU, Meteor, Pointwise Mutual Information (PMI), Dependency based methods, optimized methods based on Quadratic Assignment, etc. And the similarity methods work in different granularities - word to word, sentence to sentence, or bigger texts.


To compute the n-gram vector, just pick a value of n (say, 3), and hash every 3-word sequence in the phrase into a vector. Normalize the vector to unit length, then take the dot product of different vectors to detect similarity.
This approach has been described in J. Mitchell and M. Lapata, “Composition in Distributional Models of Semantics,” Cognitive Science, vol. 34, no. 8, pp. 1388–1429, Nov. 2010., DOI 10.1111/j.1551-6709.2010.01106.x

Thoughts
- it seems to me that keyword analysis would be enough as some of the answers of the students are mental shortcuts, where they indicate what they think is the cause in keywords, counting on the examiner understanding them. They can use keywords, because the context of their answers and their linguistic function are known, based on the questions. Hence the keywords detection algorithm should also be able to make use of question and example answers, or the text as a context that will make determining concepts behind the words more accurate, and thus increasing the accuracy of the assessment.


## To Read
- https://arxiv.org/pdf/1802.05667.pdf
- http://searchivarius.org/blog/brief-overview-querysentence-similarity-functions
- https://www.irjet.net/archives/V4/i1/IRJET-V4I129.pdf
- http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.210.9942&rep=rep1&type=pdf


## More Bibliography:


Thiede, K. W., Anderson, M. C. M., & Therriault, D. (2003). Accuracy of metacognitive monitoring affects learning of texts. Journal of Educational Psychology, 95, 66-73
De Bruin, A.B.H., Dunlosky, J., & Cavalcanti. R.B. (2017). Monitoring and regulation of learning in medical education: The need for predictive cues. Medical Education, 51, 575-58
Van Loon, M.H., De Bruin, A.B.H., Van Gog, T., & Van Merriënboer, J.J.G., & Dunlosky, J. (2014). Can students evaluate their understanding of cause-and-effect relations? The effects of diagram completion on monitoring accuracy. Acta Psychologica, 151, 143-154.
 
De Bruin, A.B.H, Kok, E.M., Lobbestael, J., & de Grip, A. (2017). The impact of an online tool for monitoring and regulating learning at university: overconfidence, learning strategy, and personality. Metacognition and Learning, 12, 21-43.
 
De Bruin, A.B.H, & van Merriënboer, J.J. (2017). Bridging Cognitive Load and Self-Regulated Learning Research: A complementary approach to contemporary issues in educational research. Learning and Instruction, 51, 1-9.