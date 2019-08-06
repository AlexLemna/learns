import argparse

print()
parser = argparse.ArgumentParser(prog="LearningArgparse")
parser.add_argument("show")
args = parser.parse_args()
print(args.show)
