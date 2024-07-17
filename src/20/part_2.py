import sys, re

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

MONSTER = set([(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)])

class Tile:
  def __init__(self, id, grid):
    self.id = id
    self.top = list(grid[0])
    self.bottom = list(grid[-1])
    self.left = [grid[i][0] for i in range(len(grid))]
    self.right = [grid[i][-1] for i in range(len(grid))]
    self.grid = [list(row) for row in grid]

  def rotate(self):
    self.top, self.right, self.bottom, self.left = self.left[::-1], self.top, self.right[::-1], self.bottom
    self.grid = list(zip(*self.grid[::-1]))

  def flip(self):
    self.top, self.right, self.bottom, self.left = self.top[::-1], self.left, self.bottom[::-1], self.right
    self.grid = [row[::-1] for row in self.grid]

tiles = set()

for i in range(0, len(lines), 12):
  id = int(re.findall("\d+", lines[i])[0])
  grid = lines[i+1:i+11]

  tiles.add(Tile(id, grid))

grid = {}
spots = set([(0, 0)])

def fits(tile, spot):
  x, y = spot

  if (x - 1, y) in grid and tile.left != grid[(x - 1, y)].right:
    return False

  if (x + 1, y) in grid and tile.right != grid[(x + 1, y)].left:
    return False

  if (x, y - 1) in grid and tile.top != grid[(x, y - 1)].bottom:
    return False

  if (x, y + 1) in grid and tile.bottom != grid[(x, y + 1)].top:
    return False

  return True

def place(tile, spot):
  x, y = spot

  for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
    nx, ny = x + dx, y + dy

    if (nx, ny) not in grid:
      spots.add((nx, ny))

  spots.remove((x, y))

  grid[(x, y)] = tile

while tiles:
  new_tiles = set()

  for tile in tiles:
    done = False

    for _ in range(4):
      for spot in spots:
        if fits(tile, spot):
          place(tile, spot)
          done = True
          break

      if done:
        break

      tile.rotate()

    if done:
      continue

    tile.flip()

    for _ in range(4):
      for spot in spots:
        if fits(tile, spot):
          place(tile, spot)
          done = True
          break

      if done:
        break

      tile.rotate()

    if done:
      continue

    new_tiles.add(tile)

  tiles = new_tiles

xs = [x[0] for x in grid.keys()]
ys = [x[1] for x in grid.keys()]

min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)

image = []

for y in range(min_y, max_y + 1):
  rows = [[] for _ in range(8)]

  for x in range(min_x, max_x + 1):
    tile = grid[(x, y)]

    for i in range(8):
      rows[i] += tile.grid[i + 1][1:-1]

  image += rows

image = Tile(0, image)

best = 0

def monsters():
  res = 0
  pixels = image.grid

  for y in range(0, len(pixels) - max(x[1] for x in MONSTER)):
    for x in range(0, len(pixels[0]) - max(x[0] for x in MONSTER)):
      if all(pixels[y + dy][x + dx] == "#" for dx, dy in MONSTER):
        res += 1

  return res

for _ in range(4):
  best = max(best, monsters())

  image.rotate()

image.flip()

for _ in range(4):
  best = max(best, monsters())

  image.rotate()

print(sum(row.count("#") for row in image.grid) - best * len(MONSTER))
