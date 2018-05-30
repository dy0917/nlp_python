# information_extraction
An information extraction task with NLTK, Stanford NER and Spacy.  
Only Python3 is supported. 

# Project Structures 
## data 
contains data and labeled data 
## jars 
stanford jar and model files
## dep 
dependency module 
## eval 
evaluation module 
## ner 
ner module 
## utils 
utilities 


# NER task 
In this repo, there are four ways to do NER tasks.

* nltk (nltk required)  
`python main_ner.py data/task nltk`


* nltk enhancement with combining continuous named entities.  
`python main_ner.py data/task enltk`


* spacy (spacy required)
Download spacy model first.  
`python -m spacy download en`  
`python main_ner.py data/task spacy` 


* Stanford NER (Java 8 required)   
`export STANFORD_MODE="jars/english.all.3class.distsim.crf.ser.gz"`   
`export STANFORD_JAR="jars/stanford-corenlp-3.9.1.jar"`   
`python main_ner.py data/task stanford` 


# NER evaluation 
There is one dataset to evaluate the performance of ners. 

* Evaluate nltk  
`python main_eval.py data/conll2003.txt nltk` 

* Evaluate spacy  
`python main_eval.py data/conll2003.txt spacy`

* Evaluate stanford   
`export STANFORD_MODE="jars/english.all.3class.distsim.crf.ser.gz"`  
`export STANFORD_JAR="jars/stanford-corenlp-3.9.1.jar"`    
`python main_eval.py data/conll2003.txt stanford` 

# TODO  

Dependency analysis, extract verbs related to named entities.
