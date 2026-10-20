import re


def normalize(t, *, casefold=True, yo2e=True):
    if yo2e:
        t = t.replace('ё', 'е').replace('Ё', 'Е')
    t = t.casefold() if casefold else t.lower()
    t = re.sub(r'\s+', ' ', t)
    return t.strip()


def tokenize(t):
    return re.findall(r'\w+(?:-\w+)*', t)


def count_freq(t):
    d = {}
    for w in t:
        d[w] = d.get(w, 0) + 1
    return d


def top_n(f, n=5):
    return sorted(f.items(), key=lambda x: (-x[1], x[0]))[:n]


t = input()
t = normalize(t)
s = tokenize(t)
f = count_freq(s)
r = top_n(f, 5)

print("Всего слов:", len(s))
print("Уникальных слов:", len(f))
print("Топ-5:")
for w, c in r:
    print(w + ":" + str(c))