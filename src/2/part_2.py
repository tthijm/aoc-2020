import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

res = 0

for line in lines:
  line = line.split(": ")
  c = line[0].split(" ")[1]
  low, high = (int(x) for x in line[0].split(" ")[0].split("-"))

  a = line[1][low - 1] == c
  b = line[1][high - 1] == c

  if (a and not b) or (not a and b):
    res += 1

print(res)
