import re
import sys

filename = sys.argv[1]

with open(filename, 'r') as file:
    content = file.read().lower()

    words = re.findall(r'\b\w+\b', content)

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_words:
        print(f'{word}: {count}')
