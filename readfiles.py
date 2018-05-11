from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import inspect, nltk, glob, os

def get_continuous_chunks(text):
    continuous_chunk = []
    for sent in nltk.sent_tokenize(text):
        chunked = nltk.ne_chunk(pos_tag(word_tokenize(sent)))
        current_chunk = []
        label = ''
        # print(chunked)
        for i in chunked:
            print(type(i))
            if type(i) == Tree:
                 # print(i.leaves(),''.join(i.label()))
                 current_chunk.append(" ".join([token for token, pos in i.leaves()]))
                 if  i.label() == 'ORGANIZATION' :
                    label = i.label()
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk and label == 'ORGANIZATION':
                    continuous_chunk.append(named_entity)
                    current_chunk = []
                    label = ''
                else:
                    current_chunk = []
            else:
                continue

        if continuous_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)


    return continuous_chunk

txt = "Jacinda Ardern is the Prime Minister of New Zealand but Roenzo isn't. But she is powerful woman."

path = 'CCAT'

ORGANIZATIONS=''
for filename in glob.glob(os.path.join(path, '2287*.txt')):
    file = open(filename, 'r')
    # print(get_continuous_chunks(file.read()))
    if ORGANIZATIONS=='':
        ORGANIZATIONS= get_continuous_chunks(file.read())
    else:
        ORGANIZATIONS=ORGANIZATIONS+get_continuous_chunks(file.read())

print(ORGANIZATIONS)
# print (get_continuous_chunks(txt))

# custom_sent_tokenizer = PunktSentenceTokenizer('Jacinda Ardern New Zealand Roenzo')

# tokenized = custom_sent_tokenizer.tokenize(txt)
# print(tokenized)
# for sent in tokenized:
#    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#       if hasattr(chunk, 'label'):
#          print(chunk.label(), ' '.join(c[0] for c in chunk))

# for sent in nltk.sent_tokenize(txt):
#    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#       if hasattr(chunk, 'label'):
#          print(chunk.label(), ' '.join(c[0] for c in chunk))
