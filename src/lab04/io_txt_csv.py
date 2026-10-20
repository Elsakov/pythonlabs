from pathlib import Path
from typing import Iterable, Sequence
import csv
import os

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    rows = list(rows)
    if rows and header is not None and len(rows[0]) != len(header):
        raise ValueError("Длина строки не совпадает с длиной заголовка")
    if rows:
        expected_len = len(rows[0])
        for r in rows:
            if len(r) != expected_len:
                raise ValueError("Все строки должны быть одинаковой длины")
    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    print("=== Тест Задания А (io_txt_csv) ===")
    temp_file = "test_temp.csv"
    data = [("яблоко", 5), ("груша", 3)]
    write_csv(data, temp_file, header=("fruit", "count"))
    print("1. write_csv: Файл успешно создан.")
    text = read_text(temp_file)
    print(f"2. read_text: Прочитано из файла:\n{text.strip()}")
    try:
        write_csv([("ошибка",)], temp_file, header=("a", "b"))
    except ValueError as e:
        print(f"3. Обработка ошибки: {e}")
    if os.path.exists(temp_file):
        os.remove(temp_file)