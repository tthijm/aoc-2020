import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

res = 0

for line in lines:
  line = line.split(": ")
  c = line[0].split(" ")[1]
  low, high = (int(x) for x in line[0].split(" ")[0].split("-"))
  v = line[1].count(c)

  if low <= v <= high:
    res += 1

print(res)
