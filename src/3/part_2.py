import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

def f(dx, dy):
  x, y = dx, dy
  res = 0

  while y < len(lines):
    if lines[y][x % len(lines[0])] == "#":
      res += 1

    x += dx
    y += dy
  
  return res

res = 1

for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
  res *= f(dx, dy)

print(res)
