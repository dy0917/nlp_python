from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from collections import Counter
import inspect, nltk, glob, os

path = 'CCAT'

def get_chunk_sent(text):
    continuous_chunk = []
    person = ''
    for sent in nltk.sent_tokenize(text):
        if 'Note' in sent:
            tagged = pos_tag(word_tokenize(sent)) 
            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            newSent = ''
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                for word, label in subtree:
                    newSent=newSent+' '+ word
            print(newSent)
            print()


for filename in glob.glob(os.path.join(path, '*.txt')):
    file = open(filename, 'r')
    get_chunk_sent(file.read())


