import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

points = set()

for y in range(len(lines)):
  for x in range(len(lines)):
    if lines[y][x] == "#":
      points.add((x, y, 0, 0))

def f(x, y, z, w):
  d = [-1, 0, 1]
  res = 0

  for dz in d:
    for dy in d:
      for dx in d:
        for dw in d:
          if dz or dy or dx or dw:
            if (x + dx, y + dy, z + dz, w + dw) in points:
              res += 1

  return res

for _ in range(6):
  min_x = min_y = min_z = min_w = 2**20
  max_x = max_y = max_z = max_w = -(2**20)
  new_points = set()

  for x, y, z, w in points:
    min_x, max_x = min(min_x, x), max(max_x, x)
    min_y, max_y = min(min_y, y), max(max_y, y)
    min_z, max_z = min(min_z, z), max(max_z, z)
    min_w, max_w = min(min_w, w), max(max_w, w)

  for w in range(min_w - 5, max_w + 6):
    for z in range(min_z - 5, max_z + 6):
      for y in range(min_y - 5, max_y + 6):
        for x in range(min_x - 5, max_x + 6):
          if (x, y, z, w) in points:
            if 2 <= f(x, y, z, w) <= 3:
              new_points.add((x, y, z, w))
          else:
            if f(x, y, z, w) == 3:
              new_points.add((x, y, z, w))

  points = new_points

print(len(points))
