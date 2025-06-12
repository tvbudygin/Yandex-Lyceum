import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--name")
parser.add_argument("-up", "--up_case", action="store_true", help="Превращать имя в верхний регистр")
parser.add_argument("--number", choices=[0, 1, 2], type=int, default=0, help="Выбор номера",
                    required=True)
parser.add_argument("--no-name", action="store_const", const="no", dest="name")

args = parser.parse_args()
name = args.name
if (args.up_case):
    name = name.upper()
print(f"Наше имя: {name}. И наш номер: {args.number}")