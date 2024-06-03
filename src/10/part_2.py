import sys, functools

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = set(int(x) for x in lines)

high = max(lines)

@functools.cache
def f(x):
  if x == high:
    return 1

  total = 0

  for d in [1, 2, 3]:
    if x + d in lines:
      total += f(x + d)

  return total

print(f(0))
