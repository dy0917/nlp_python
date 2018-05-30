from nltk import sent_tokenize, word_tokenize


def tokenize(text):
    sents = sent_tokenize(text)
    tokenized_sents = [word_tokenize(sent) for sent in sents]
    return tokenized_sents


class NERNotFound(Exception):
    pass
