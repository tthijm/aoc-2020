import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = set(int(x) for x in lines)

low = min(lines)
high = max(lines)

ones = threes = 0
i = 0

while i != high:
  if i + 1 in lines:
    ones += 1
    i += 1
  elif i + 2 in lines:
    i += 2
  elif i + 3 in lines:
    threes += 1
    i += 3
  else:
    assert False

print(ones * (threes + 1))
