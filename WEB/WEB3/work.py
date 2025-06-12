import argparse


def count_lines(fil):
    try:
        with open(fil) as f:
            return len(f.readlines())
    except Exception:
        return 0


parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str)
args = parser.parse_args()
if args.file:
    if len(args.file) > 0:
        print(count_lines(args.file))
