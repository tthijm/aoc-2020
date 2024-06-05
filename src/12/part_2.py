import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

DELTAS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
DIRS = ["E", "S", "W", "N"]
x = y = 0
wx, wy = 10, 1

for line in lines:
  c = line[0]
  n = int(line[1:])

  if c in DIRS:
    dx, dy = DELTAS[DIRS.index(c)]
    wx += n * dx
    wy += n * dy
  elif c == "L":
    for _ in range(n // 90):
      wx, wy = -wy, wx
  elif c == "R":
    for _ in range(n // 90):
      wx, wy = wy, -wx
  else:
    x += n * wx
    y += n * wy

print(abs(x) + abs(y))
