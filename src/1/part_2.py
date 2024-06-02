import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = set(int(x) for x in lines)

for a in lines:
  for b in lines:
    c = 2020 - a - b

    if c in lines:
      print(a * b * c)
      exit(0)
