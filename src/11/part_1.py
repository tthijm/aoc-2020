import sys, copy

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

DIRS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
lines = [[c for c in line] for line in lines]

while True:
  new_lines = copy.deepcopy(lines)

  for y in range(len(lines)):
    for x in range(len(lines[0])):
      if lines[y][x] == "L":
        if not any(0 <= x + dx < len(lines[0]) and 0 <= y + dy < len(lines) and lines[y + dy][x + dx] == "#" for dx, dy in DIRS):
          new_lines[y][x] = "#"
      elif lines[y][x] == "#":
        if sum(0 <= x + dx < len(lines[0]) and 0 <= y + dy < len(lines) and lines[y + dy][x + dx] == "#" for dx, dy in DIRS) >= 4:
          new_lines[y][x] = "L"

  if new_lines == lines:
    break

  lines = new_lines

res = 0

for line in lines:
  res += line.count("#")

print(res)
