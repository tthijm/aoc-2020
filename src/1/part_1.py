import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = set(int(x) for x in lines)

for v in lines:
  a = 2020 - v

  if a in lines:
    print(v * a)
    break
