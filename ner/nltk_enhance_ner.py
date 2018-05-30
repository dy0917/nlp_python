from nltk import pos_tag, ne_chunk
from nltk.tree import Tree
from utils import tokenize


def nltk_enhance_ner(text):
    tokenized_sents = tokenize(text)
    orgs = []
    for (index, words) in enumerate(tokenized_sents):
        _orgs = extract_orgs(words)
        orgs.extend([(index, org) for org in _orgs])
    return orgs


def extract_orgs(words):
    orgs = []
    pos_words = pos_tag(words)
    current_entity = []
    labels = []
    for trunk in ne_chunk(pos_words):
        label, entity = extract_entity(trunk)
        if label and entity:
            labels.append(label)
            current_entity.append(entity)
        else:
            if current_entity and "ORGANIZATION" in labels:
                orgs.append(" ".join(current_entity))
            current_entity = []
            labels = []
    return orgs


def extract_entity(trunk):
    if isinstance(trunk, Tree):
        label = trunk.label()
        entity = " ".join([l[0] for l in trunk])
    else:
        label = None
        entity = None
    return label, entity
