# start CoreNLPServer
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
from nltk.parse.corenlp import CoreNLPDependencyParser


def dep_parse(sents, entity):
    dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
    parsers = dep_parser.raw_parse_sents(sents)
    deps = []
    for (parser,) in parsers:
        for governor, dep, dependent in parser.triples():
            is_dep_verb = (
                (governor[0] in entity and dependent[1].startswith("VB")) or
                (dependent[0] in entity and governor[1].startswith("VB"))
            )
            if is_dep_verb:
                deps.append((governor, dep, dependent))
    return deps


sents = [
    'Anhalt said children typically treat a 20-ounce soda bottle as one ',
    'serving, while it actually contains 2 1/2 servings.'
]

deps = dep_parse(sents, "Anhalt")
print(deps)
