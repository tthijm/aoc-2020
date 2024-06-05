import sys, re

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

ranges = []

for line in lines[:lines.index("")]:
  nums = [int(x) for x in re.findall("\d+", line)]

  ranges.append(nums)

res = 0

for line in lines[lines.index("nearby tickets:") + 1:]:
  for x in line.split(","):
    x = int(x)
    valid = False

    for r in ranges:
      if r[0] <= x <= r[1] or r[2] <= x <= r[3]:
        valid = True
        break
    
    if not valid:
      res += x

print(res)
