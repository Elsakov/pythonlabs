#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from pathlib import Path

try:
    from src.lib.text import normalize, tokenize, count_freq, top_n
except ImportError:
    raise ImportError(
        "Не найден модуль src.lib.text. "
        "Убедитесь, что ЛР3 выполнена и файл src/lib/text.py существует."
    )

def cmd_stats(args: argparse.Namespace) -> None:
    input_path = Path(args.input)
    if not input_path.is_file():
        sys.exit(f"Ошибка: файл '{input_path}' не найден.")

    text = input_path.read_text(encoding="utf-8")
    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)
    top = top_n(freq, args.top)

    print(f"Топ-{args.top} слов в файле '{input_path}':")
    for word, count in top:
        print(f"{word:>15} : {count}")


def cmd_cat(args: argparse.Namespace) -> None:
    input_path = Path(args.input)
    if not input_path.is_file():
        sys.exit(f"Ошибка: файл '{input_path}' не найден.")

    with input_path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            if args.n:
                print(f"{lineno:>6}\t{line}", end="")
            else:
                print(line, end="")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cli_text",
        description="CLI-утилита для анализа текста и вывода файла (ЛР6).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    stats_parser = subparsers.add_parser("stats", help="Частотный анализ слов.")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу.")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов вывести.")
    stats_parser.set_defaults(func=cmd_stats)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла.")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу.")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки.")
    cat_parser.set_defaults(func=cmd_cat)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        parser.error(f"Ошибка выполнения: {e}")


if __name__ == "__main__":
    main()