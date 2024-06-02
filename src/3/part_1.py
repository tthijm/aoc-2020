import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

x, y = 3, 1
res = 0

while y < len(lines):
  if lines[y][x % len(lines[0])] == "#":
    res += 1

  x += 3
  y += 1

print(res)
