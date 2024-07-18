import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

DIRS = { "e": (2, 0), "se": (1, 1), "sw": (-1, 1), "w": (-2, 0), "nw": (-1, -1), "ne": (1, -1) }

black = set()

for line in lines:
  i = 0
  x, y = 0, 0

  while i < len(line):
    if line[i:i+2] in DIRS.keys():
      dx, dy = DIRS[line[i:i+2]]
      i += 2
    else:
      dx, dy = DIRS[line[i]]
      i += 1

    x, y = x + dx, y + dy
  
  if (x, y) not in black:
    black.add((x, y))
  else:
    black.remove((x, y))

print(len(black))
