# language: python, file: src/lab05/json_csv.py
import csv
import json
import os

def p(a, b):
    print(a)
    print(f"data > out > {os.path.basename(b)}")
    with open(b, encoding="utf-8") as f:
        l = f.read().splitlines()
        w = len(str(len(l)))
        for i, x in enumerate(l, 1):
            print(f"{i:<{w}}   {x}")
    print()

def j(a, b):
    with open(a, encoding="utf-8") as f:
        d = json.load(f)
        
    # Проверка 1 и 2
    if not isinstance(d, list) or len(d) == 0:
        raise ValueError("пустой JSON или неподдерживаемая структура")
    for x in d:
        if not isinstance(x, dict):
            raise ValueError("Элемент списка не является словарем")

    k = d[0].keys()
    with open(b, "w", encoding="utf-8", newline="") as f:
        r = csv.DictWriter(f, fieldnames=k)
        r.writeheader()
        r.writerows(d)

def c(a, b):
    with open(a, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        # Проверка 3 (нет заголовка)
        if not r.fieldnames:
            raise ValueError("CSV без заголовка или пустой")
        d = list(r)
        
    if len(d) == 0:
        raise ValueError("CSV без заголовка или пустой")

    with open(b, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    j("src/data/samples/people.json", "src/data/samples/o1.csv")
    p("Результат JSON -> CSV", "src/data/samples/o1.csv")
    
    c("src/data/samples/people.csv", "src/data/samples/o2.json")
    p("Результат CSV -> JSON", "src/data/samples/o2.json")