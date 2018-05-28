from nltk import pos_tag, ne_chunk
from nltk.chunk import tree2conllstr


def annotate_org(tokenized_sent):
    pos_tokenized_sent = pos_tag(tokenized_sent)
    prediction = tree2conllstr(ne_chunk(pos_tokenized_sent))
    named_entities = [
        key for (index, key) in enumerate(prediction.split()) if index % 3 != 1
    ]
    tokens = named_entities[0::2]
    annotations = list(map(
        lambda item: "ORG" if "ORGANIZATION" in item else "O",
        named_entities[1::2]))

    ne_pairs = list(zip(tokens, annotations))
    return ne_pairs
