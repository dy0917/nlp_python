from collections import Counter, defaultdict
import os
from utils import NERNotFound


def main(data_dir, recognizer):
    filepaths = [os.path.join(data_dir, name) for name in os.listdir(data_dir)]
    ner = get_ner(recognizer)
    orgs, indexes = process_ner(ner, filepaths)
    save_result(orgs, indexes, ner.__name__)


def get_ner(recognizer):
    if recognizer == "nltk":
        from ner.nltk_ner import nltk_ner as ner
    elif recognizer == "stanford":
        from ner.stanford_ner import stanford_ner as ner
    elif recognizer == "enltk":
        from ner.nltk_enhance_ner import nltk_enhance_ner as ner
    elif recognizer == "spacy":
        from ner.spacy_ner import spacy_ner as ner
    else:
        raise NERNotFound("ner not found")
    return ner


def process_ner(ner, filepaths):
    file_count = len(filepaths)
    orgs = []
    indexes = defaultdict(dict)
    for (i, filepath) in enumerate(filepaths):
        filename = os.path.basename(filepath)
        text = open(filepath).read()
        print(f"{ner.__name__} is processing file {filename}, {i}/{file_count} completed", flush=True)
        orgs_tuple = ner(text)
        for (index, org) in orgs_tuple:
            orgs.append(org)
            if filename not in indexes[org]:
                indexes[org][filename] = {index}
            else:
                indexes[org][filename].add(index)
    return orgs, indexes


def save_result(orgs, indexes, ner_name):
    counter = Counter(orgs)
    result_dir = "result"
    try:
        os.mkdir(result_dir)
    except:
        pass
    orgs_file = os.path.join(result_dir, f"{ner_name}_orgs.csv")
    indexes_file = os.path.join(result_dir, f"{ner_name}_indexes.csv")
    print(f"organizations are saved into {orgs_file}")
    print(f"sentense indexes are saved into {indexes_file}")

    with open(orgs_file, "w") as f_org, open(indexes_file, "w") as f_index:
        for (org, cnt) in counter.most_common():
            f_org.write(f"{org},{cnt}\n")
            _indexes = indexes[org]
            for (filename, items) in _indexes.items():
                _indexes = ",".join([str(index) for index in items])
                f_index.write(f"{org},{filename},{_indexes}\n")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("usage: python main_ner.py data_dir recognizer")
    else:
        data_dir, recognizer = sys.argv[1], sys.argv[2]
        main(data_dir, recognizer)
