import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1")
parser.add_argument("arg2", nargs='*')
args = parser.parse_args()
print(args.arg1, *args.arg2)
