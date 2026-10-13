import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))
from text import get_words, get_word_counts
s = "привет, мир! Привет!!!"
w = get_words(s)
c = get_word_counts(w)
a = len(w)
b = len(c)
print(f"Всего слов: {a}")
print(f"Уникальных слов: {b}")
print("Топ-5:")
for k, v in c.most_common(5):
    print(f"{k}:{v}")