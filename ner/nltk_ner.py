from nltk import pos_tag, ne_chunk
from nltk.tree import Tree
from utils import tokenize


def nltk_ner(text):
    tokenized_sents = tokenize(text)
    orgs = []
    for (index, tokenized_sent) in enumerate(tokenized_sents):
        _orgs = extract_orgs(tokenized_sent)
        orgs.extend([(index, org) for org in _orgs])
    return orgs


def extract_orgs(tokenized_sent):
    orgs = []
    pos_tokenized_sent = pos_tag(tokenized_sent)
    for trunk in ne_chunk(pos_tokenized_sent):
        if isinstance(trunk, Tree):
            label = trunk.label()
            if label == "ORGANIZATION":
                org = " ".join([l[0] for l in trunk])
                orgs.append(org)
    return orgs
