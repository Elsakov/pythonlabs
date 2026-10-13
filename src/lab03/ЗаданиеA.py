import re
from collections import Counter
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text=text.casefold()
    else:
        text=text.lower()
    if yo2e:
        text=text.replace('ё', 'е')
    text = re.sub(r'[\t\r\n]+', ' ', text)
    text = re.sub(r' +', ' ', text).strip()
    return text
def tokenize(text: str) -> list[str]:
    p=r'\w+(?:-\w+)*'
    w=re.findall(p, text)
    return w
def count_freq(tokens: list[str]) -> dict[str, int]:
    c = Counter(tokens)          
    r = dict(c)            
    return r
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sw=sorted(freq.items(), key=lambda pa: (-pa[1], pa[0]))
    return sw
print("normalize")
print('  "ПриВЕт\\nМИР\\t"   ->', repr(normalize("ПриВЕт\nМИР\t")))
print('  "ёжик, Ёлка"      ->', repr(normalize("ёжик, Ёлка")))
print('  "Hello\\r\\nWorld" ->', repr(normalize("Hello\r\nWorld")))
print('  "  двойные   пробелы  " ->', repr(normalize("  двойные   пробелы  ")))
print()

print("tokenize (предполагаем, что текст уже normalize)")
print('  "привет мир"          ->', tokenize("привет мир"))
print('  "hello,world!!!"      ->', tokenize("hello,world!!!"))
print('  "по-настоящему круто" ->', tokenize("по-настоящему круто"))
print('  "2025 год"            ->', tokenize("2025 год"))
print('  "emojis 😀 не слово"  ->', tokenize("emojis 😀 не слово"))
print()

print("count_freq + top_n")
tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
print('  Токены ["a","b","a","c","b","a"] -> частоты', freq1)
print('  top_n(..., n=2) ->', top_n(freq1, 2))
print()

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = count_freq(tokens2)
print('  Токены ["bb","aa","bb","aa","cc"] -> частоты', freq2)
print('  top_n(..., n=2) ->', top_n(freq2, 2))
