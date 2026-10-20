from pathlib import Path
import sys
from collections import Counter

# Добавляем src/ в sys.path, чтобы работали импорты
SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lib.text import normalize, tokenize, top_n
from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir

def main():
    input_path = "data/lab04/input.txt"
    output_path = "data/lab04/report.csv"
    
    # Читаем текст (используя функцию из Задания А)
    text = read_text(input_path)
    
    # Считаем слова
    tokens = tokenize(normalize(text))
    freq = dict(Counter(tokens))
    rows = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    
    # Записываем отчет (используя функцию из Задания А)
    ensure_parent_dir(output_path)
    write_csv(rows, output_path, header=("word", "count"))
    
    total_words = sum(freq.values())
    unique_words = len(freq)
    top5 = top_n(freq, 5)
    
    # Выводим результат в консоль
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()