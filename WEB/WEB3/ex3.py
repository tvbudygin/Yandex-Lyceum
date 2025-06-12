import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("integer", nargs='*', metavar="Целые числа",
                    type=str, help="Перевод двоичных чисел в десятичные")
parser.add_argument("--base", default=2, type=int, help="Оснавание системы счисления")
parser.add_argument("--log", default=sys.stdout, type=argparse.FileType("a"),
                    help="Запись результата в файл")
args = parser.parse_args()
result = " ".join(map(lambda x: str(int(x, args.base)), args.integer))
args.log.write(result + "\n")
args.log.close()