from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from collections import Counter
import inspect, nltk, glob, os

def get_continuous_chunks(text):
    continuous_chunk = []
    person = ''
    for sent in nltk.sent_tokenize(text):
        chunked = nltk.ne_chunk(pos_tag(word_tokenize(sent)))
        selectedChunk= []
        for i in chunked: 
            if type(i) == Tree:
                 if  i.label() == 'ORGANIZATION' or i.label() == 'PERSON':
                    selectedChunk.append(i)
        
            else:
                hasOrg = False
                for i in selectedChunk:
                    if  i.label() == 'ORGANIZATION':
                        hasOrg = True
                if  hasOrg == True:
                    current_chunk=[]
                    for i in selectedChunk:
                        current_chunk.append(" ".join([token for token, pos in i.leaves()]))
                    entity=" ".join(current_chunk)
                    if entity not in continuous_chunk and entity!='':
                        continuous_chunk.append(entity)
    return continuous_chunk

txt = "Jacinda Ardern is the Prime Minister of New Zealand but Roenzo isn't. But she is powerful woman."

path = 'CCAT'

ORGANIZATIONS=''
for filename in glob.glob(os.path.join(path, '*.txt')):
    file = open(filename, 'r')
    # print(get_continuous_chunks(file.read()))
    if ORGANIZATIONS=='':
        ORGANIZATIONS= get_continuous_chunks(file.read())
    else:
        ORGANIZATIONS=ORGANIZATIONS+get_continuous_chunks(file.read())

for name,amount in Counter(ORGANIZATIONS).most_common():
    if(amount> 10):
        print(name,amount)

print(Counter(ORGANIZATIONS).most_common(5))


def get_chunk_sent(text):
    continuous_chunk = []
    person = ''
    for sent in nltk.sent_tokenize(text):
        chunked = nltk.ne_chunk(pos_tag(word_tokenize(sent)))
        selectedChunk= []
        for i in chunked: 
            if type(i) == Tree:
                 if  i.label() == 'ORGANIZATION' or i.label() == 'PERSON':
                    selectedChunk.append(i)
        
            else:
                hasOrg = False
                for i in selectedChunk:
                    if  i.label() == 'ORGANIZATION':
                        hasOrg = True
                if  hasOrg == True:
                    current_chunk=[]
                    for i in selectedChunk:
                        current_chunk.append(" ".join([token for token, pos in i.leaves()]))
                    entity=" ".join(current_chunk)
                    if entity not in continuous_chunk and entity!='':
                        continuous_chunk.append(entity)
    return continuous_chunk