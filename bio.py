from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import inspect, nltk, glob, os

def get_continuous_chunks(tagged_sent):
    continuous_chunk = []
    current_chunk = []

    for token, tag in tagged_sent:
        if tag != "O":
            current_chunk.append((token, tag))
        else:
            if current_chunk: # if the current chunk is not empty
                continuous_chunk.append(current_chunk)
                current_chunk = []
    # Flush the final current_chunk into the continuous_chunk, if any.
    if current_chunk:
        continuous_chunk.append(current_chunk)
    return continuous_chunk

ne_tagged_sent = [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'), ('at', 'O'), ('Stony', 'ORGANIZATION'), ('Brook', 'ORGANIZATION'), ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'LOCATION')]

named_entities = get_continuous_chunks(ne_tagged_sent)
named_entities = get_continuous_chunks(ne_tagged_sent)
named_entities_str = [" ".join([token for token, tag in ne]) for ne in named_entities]
named_entities_str_tag = [(" ".join([token for token, tag in ne]), ne[0][1]) for ne in named_entities]

print(named_entities)
print()
print(named_entities_str)
print()
print(named_entities_str_tag)
print()