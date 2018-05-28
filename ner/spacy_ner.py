import spacy
from nltk import sent_tokenize
nlp = spacy.load("en")


def spacy_ner(text):
    sents = sent_tokenize(text)
    orgs = []
    for (index, sent) in enumerate(sents):
        _orgs = extract_orgs(sent)
        orgs.extend([(index, org) for org in _orgs])
    return orgs


def extract_orgs(sent):
    orgs = []
    doc = nlp(sent)
    for entity in doc.ents:
        if entity.label_ == "ORG":
            orgs.append(entity.text.strip())
    return orgs


if __name__ == "__main__":
    text = open("../CCAT/4242newsML.txt").read()
    orgs = spacy_ner(text)
    print(orgs)
