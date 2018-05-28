from nltk.tag import StanfordNERTagger
from utils import tokenize
import os

model_dir = os.getenv("STANFORD_MODEL")
jar_dir = os.getenv("STANFORD_JAR")
stanford_tagger = StanfordNERTagger(model_dir, jar_dir)


def stanford_ner(text):
    tokenized_sents = tokenize(text)
    orgs = []
    for (index, words) in enumerate(tokenized_sents):
        _orgs = extract_orgs(words)
        orgs.extend([(index, org) for org in _orgs])
    return orgs


def extract_orgs(words):
        current = []
        orgs = []
        for (word, label) in stanford_tagger.tag(words):
            if label == "ORGANIZATION":
                current.append(word)
            elif label == "O" and current:
                org = " ".join(current)
                orgs.append(org)
                current = []
        if current:
            org = " ".join(current)
            orgs.append(org)
        return orgs
