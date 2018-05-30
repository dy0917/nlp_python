import os
from nltk.tag import StanfordNERTagger
model_dir = os.getenv("STANFORD_MODEL")
jar_dir = os.getenv("STANFORD_JAR")
stanford_tagger = StanfordNERTagger(model_dir, jar_dir)


def annotate_org(tokenized_sent):
    tags = []
    tokens = []
    for (token, label) in stanford_tagger.tag(tokenized_sent):
        if label == "ORGANIZATION":
            tags.append("ORG")
        else:
            tags.append("O")
        tokens.append(token)
    return list(zip(tokens, tags))
