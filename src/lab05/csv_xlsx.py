
import csv
import os
from openpyxl import Workbook

def x(a, b):
    with open(a, encoding="utf-8", newline="") as f:
        r = list(csv.reader(f))
        

    if len(r) == 0 or len(r[0]) == 0:
        raise ValueError("CSV без заголовка или пустой")

    w = Workbook()
    s = w.active
    for v in r:
        s.append(v)
    w.save(b)
    
    print("Результат CSV -> XLSX")
    print(f"data > out > {os.path.basename(b)}")
    print(f"Файл успешно создан. Строк: {len(r)}")
    print()

if __name__ == "__main__":
    x("src/data/samples/cities.csv", "src/data/samples/o3.xlsx")