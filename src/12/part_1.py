import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

DELTAS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
DIRS = ["E", "S", "W", "N"]
x = y = 0
i = 0

for line in lines:
  c = line[0]
  n = int(line[1:])

  if c in DIRS:
    dx, dy = DELTAS[DIRS.index(c)]
    x += n * dx
    y += n * dy
  elif c == "L":
    i = (i - n // 90) % len(DELTAS)
  elif c == "R":
    i = (i + n // 90) % len(DELTAS)
  else:
    dx, dy = DELTAS[i]
    x += n * dx
    y += n * dy

print(abs(x) + abs(y))
