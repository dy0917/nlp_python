from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from collections import Counter
from itertools import groupby
import inspect, nltk, glob, os


for tag, chunk in groupby(netagged_words, lambda x:x[1]):
    if tag != "O":
        print("%-12s"%tag, " ".join(w for w, t in chunk))


def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    #print(chunked)
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk

# txt = "Jacinda Ardern is the Prime Minister of New Zealand but Roenzo isn't."
def getAnlysis():
    path = 'CCAT'
    continuous_chunk = []
    for filename in glob.glob(os.path.join(path, '*.txt')):
        file = open(filename, 'r')

        for sent in nltk.sent_tokenize(file.read()):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'label'):
                    if chunk.label()=='ORGANIZATION':
                        continuous_chunk.append(''.join(c[0] for c in chunk))
    for i,j in Counter(continuous_chunk).most_common():
        print(j,i)

getAnlysis()
        # message=file.read()
        # if txt=='':
        #     txt= get_continuous_chunks(file.read())
        #     print(txt)
        # else:
        #     txt=txt+get_continuous_chunks(file.read())


# for sent in nltk.sent_tokenize(message):
#    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#       if hasattr(chunk, 'label'):
#          print(chunk.label(), ' '.join(c[0] for c in chunk))



# 225 NOTE
# 161 Reuters
# 107 Parent
# 62 LATEST
# 59 Bank
# 55 PCT
# 46 ValuJet
# 45 TYPE
# 45 MLN
# 44 BET
# 41 CompuSe