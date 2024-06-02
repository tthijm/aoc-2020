import sys, collections, re

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

edges = collections.defaultdict(list)

for line in lines:
  x = re.findall("([a-z]+ [a-z]+) bags?", line)

  for edge in x[1:]:
    edges[edge].append(x[0])

res = 0
s = ["shiny gold"]
seen = set()

while s:
  k = s.pop()

  for edge in edges[k]:
    if edge not in seen:
      s.append(edge)
      seen.add(edge)
      res += 1

print(res)
