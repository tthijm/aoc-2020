import sys, collections, re

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

edges = collections.defaultdict(list)

for line in lines:
  name = f"{line.split()[0]} {line.split()[1]}"
  line = " ".join(line.split()[3:])
  x = re.findall("(\d+ [a-z]+ [a-z]+) bags?", line)

  for v in x:
    n = int(v.split()[0])
    v = " ".join(v.split()[1:])

    edges[name].append((n, v))

def f(k):
  if k not in edges:
    return 0
  
  res = 0

  for n, v in edges[k]:
    res += n
    res += n * f(v)
  
  return res

print(f("shiny gold"))
