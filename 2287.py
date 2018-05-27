from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from collections import Counter
import inspect, nltk, glob, os

def get_continuous_chunks(text):
    continuous_chunk = []
    curentEntity= []
    person = ''
    for sent in nltk.sent_tokenize(text):

        chunked = nltk.ne_chunk(pos_tag(word_tokenize(sent)))
  
        for i in chunked:
            current_chunk = []
            if type(i) == Tree:
                 # print(i.leaves(),''.join(i.label()))
                 current_chunk.append(" ".join([token for token, pos in i.leaves()]))
                 # print(previous)
                 if  i.label() == 'ORGANIZATION' or i.label() == 'PERSON':
                    curentEntity = curentEntity + current_chunk
        
            else:
                entity=" ".join(curentEntity)
                curentEntity=[]
                if entity not in continuous_chunk and entity!='':
                    continuous_chunk.append(entity)
                # previous=''

    return continuous_chunk

txt = "Jacinda Ardern is the Prime Minister of New Zealand but Roenzo isn't. But she is powerful woman."

path = 'CCAT'

ORGANIZATIONS=''
for filename in glob.glob(os.path.join(path, '2321*.txt')):
    file = open(filename, 'r')
    # print(get_continuous_chunks(file.read()))
    if ORGANIZATIONS=='':
        ORGANIZATIONS= get_continuous_chunks(file.read())
    else:
        ORGANIZATIONS=ORGANIZATIONS+get_continuous_chunks(file.read())

for name,amount in Counter(ORGANIZATIONS).most_common():
    print(name,amount)

