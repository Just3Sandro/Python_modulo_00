import sys
import re

def filter_words(sentense, min_lenght):
    words = re.findall(r'\w+', sentence)

    filtered_words = [word for word in words if len(word) >= min_lenght]

    return filtered_words

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        sentence = sys.argv[1]
        min_lenght = int(sys.argv[2])
        filtered_words = filter_words(sentence, min_lenght)
        print(filtered_words)
