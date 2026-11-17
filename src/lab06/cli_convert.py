import argparse
import sys
import inspect
from pathlib import Path
try:
    from src.lab05.json_csv import j as json_to_csv, c as csv_to_json
except ImportError as e:
    print(f" Ошибка: Не удалось импортировать функции j и c из src/lab05/json_csv.py\nДетали: {e}")
    sys.exit(1)
csv_to_xlsx = None
try:
    import src.lab05.csv_xlsx as cx_mod
    for name, obj in inspect.getmembers(cx_mod):
        if inspect.isfunction(obj) and not name.startswith('_'):
            if len(inspect.signature(obj).parameters) == 2:
                csv_to_xlsx = obj
                break
except ImportError:
    pass

def cmd_json2csv(args: argparse.Namespace) -> None:
    in_path, out_path = Path(args.input), Path(args.output)
    if not in_path.is_file():
        sys.exit(f"Ошибка: входной файл '{in_path}' не найден.")
    try:
        json_to_csv(str(in_path), str(out_path))
        print(f"JSON → CSV: {in_path} → {out_path}")
    except Exception as e:
        sys.exit(f" Ошибка конвертации: {e}")

def cmd_csv2json(args: argparse.Namespace) -> None:
    in_path, out_path = Path(args.input), Path(args.output)
    if not in_path.is_file():
        sys.exit(f"Ошибка: входной файл '{in_path}' не найден.")
    try:
        csv_to_json(str(in_path), str(out_path))
        print(f"CSV → JSON: {in_path} → {out_path}")
    except Exception as e:
        sys.exit(f" Ошибка конвертации: {e}")

def cmd_csv2xlsx(args: argparse.Namespace) -> None:
    if csv_to_xlsx is None:
        sys.exit(" Ошибка: В файле src/lab05/csv_xlsx.py не найдена функция с 2 аргументами.")
    in_path, out_path = Path(args.input), Path(args.output)
    if not in_path.is_file():
        sys.exit(f"Ошибка: входной файл '{in_path}' не найден.")
    try:
        csv_to_xlsx(str(in_path), str(out_path))
        print(f"CSV → XLSX: {in_path} → {out_path}")
    except Exception as e:
        sys.exit(f" Ошибка конвертации: {e}")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cli_convert", description="CLI-конвертер (ЛР6).")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_j2c = subparsers.add_parser("json2csv", help="JSON в CSV.")
    p_j2c.add_argument("--in", dest="input", required=True)
    p_j2c.add_argument("--out", dest="output", required=True)
    p_j2c.set_defaults(func=cmd_json2csv)

    p_c2j = subparsers.add_parser("csv2json", help="CSV в JSON.")
    p_c2j.add_argument("--in", dest="input", required=True)
    p_c2j.add_argument("--out", dest="output", required=True)
    p_c2j.set_defaults(func=cmd_csv2json)

    p_c2x = subparsers.add_parser("csv2xlsx", help="CSV в XLSX.")
    p_c2x.add_argument("--in", dest="input", required=True)
    p_c2x.add_argument("--out", dest="output", required=True)
    p_c2x.set_defaults(func=cmd_csv2xlsx)

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