if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("usage: python main_eval.py data_file recognizer")
    else:
        dataset = sys.argv[1]
        recognizer = sys.argv[2]
        from eval import evaluate
        evaluate(dataset, recognizer)
