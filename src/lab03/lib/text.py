import re
from collections import Counter

def get_words(t):
    return re.findall(r'\w+', t.lower())

def get_word_counts(w):
    return Counter(w)