import spacy
nlp = spacy.load("en")


def annotate_org(tokenized_sent):
    sent = " ".join(tokenized_sent)
    doc = nlp(sent)
    annotations = []
    for item in doc:
        text = item.text.strip()
        tag = item.ent_type_
        if tag != "ORG":
            tag = "O"
        annotations.append((text, tag))
    return annotations
