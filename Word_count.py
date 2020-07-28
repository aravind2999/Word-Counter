import re
from collections import Counter
def count_words(path):
    with open(path, encoding = 'utf-8') as file:
        all_words = re.findall("[0-9a-zA-Z']+", file.read())
        all_words = [word.upper() for word in all_words]
        print('Total Number of Words:',len(all_words))

        word_counts = Counter()
        for word in all_words:
            word_counts[word] += 1
        print('Top 10 words:')
        for word in word_counts.most_common(10):
            print(word[0], " ", word[1] )

if __name__ = '__main__':
    count_words("C:\Users\ARAVIND REDDY\Documents\New Text Document.txt")
