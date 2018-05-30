from nltk.metrics.scores import accuracy, precision, recall, f_measure
import os


def process_test_data(filename):
    name_entities = []
    with open(filename) as f:
        for line in f:
            try:
                token, _, _, tag = line.strip().split()
            except:
                pass
            else:
                if "ORG" in tag:
                    tag = "ORG"
                else:
                    tag = "O"
                name_entities.append((token, tag))
    return name_entities


def extract_sents(filename):
    sents = []
    current_sent = []
    with open(filename) as f:
        for line in f:
            try:
                token, _, _, tag = line.strip().split()
            except:
                pass
            else:
                current_sent.append(token)
                if token == "." and tag == "O":
                    sents.append(current_sent)
                    current_sent = []
    return sents


def annotate(tokenized_sents, annotate_method):
    annotations = []
    count = len(tokenized_sents)
    for (index, tokenize_sent) in enumerate(tokenized_sents):
        print(f"processing {index}/{count} sentenses")
        result = annotate_method(tokenize_sent)
        annotations.extend(result)
    return annotations


def keep_same_length(reference, test):
    ref_tokens = [token for (token, _) in reference]
    test_tokens = [token for (token, _) in test]
    removed_ref = []
    common_tokens = set(ref_tokens).intersection(set(test_tokens))
    for (index, token) in enumerate(ref_tokens):
        if token not in common_tokens:
            removed_ref.append(reference[index])
    for item in removed_ref:
        reference.remove(item)

    index = 0
    for index in range(len(reference)):
        while test[index][0] != reference[index][0]:
            del test[index]


def get_measures(reference, test):
    tp = tn = fp = fn = 0

    for ((_, r), (_, t)) in zip(reference, test):
        if r == t == "O":
            tn += 1
        elif r == t == "ORG":
            tp += 1
        elif r == "O" and t == "ORG":
            fp += 1
        elif r == "ORG" and t == "O":
            fn += 1
    matrix = [tp, tn, fp, fn]
    acc = accuracy(reference, test)
    reference_set = set(reference)
    test_set = set(test)
    pre = precision(reference_set, test_set)
    rec = recall(reference_set, test_set)
    f = f_measure(reference_set, test_set)
    return acc, pre, rec, f, matrix


def save_result(reference, test, ref_file, test_file):
    keep_same_length(reference, test)
    print(f"ground truth in {ref_file}")
    print(f"predictions in {test_file}")
    with open(ref_file, "w") as f:
        list(map(lambda item: f.write(" ".join(item) + "\n"), reference))
    with open(test_file, "w") as f:
        list(map(lambda item: f.write(" ".join(item) + "\n"), test))


def evaluate(dataset, recognizer):
    name_entities = process_test_data(dataset)
    sents = extract_sents(dataset)
    result_dir = "evaluation"
    result_file = os.path.join(result_dir, "eval_result.txt")
    try:
        os.mkdir(result_dir)
    except:
        pass
    if recognizer == "nltk":
        from .eval_nltk import annotate_org
    elif recognizer == "stanford":
        from .eval_stanford import annotate_org
    else:
        from .eval_spacy import annotate_org
    predicted_name_entities = annotate(sents, annotate_org)
    ref_file = os.path.join(result_dir, "eval_ref.txt")
    test_file = os.path.join(result_dir, "eval_test.txt")
    save_result(name_entities, predicted_name_entities, ref_file, test_file)
    acc, pre, rec, f, matrix = get_measures(name_entities, predicted_name_entities)
    print(f"evaluate result are saved into {result_file}")
    open(result_file, "a").write(
        f"{recognizer} evaluation on {dataset}, accuracy={acc}, precision={pre}, recall={rec}, f_measure={f}, matrix={matrix}\n")
