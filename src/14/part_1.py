import sys, collections, re

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

mem = collections.defaultdict(int)
mask = None

def f(x):
  res = ""

  for i in range(len(mask) - 1, -1, -1):
    if mask[len(mask) - 1 - i] == "X":
      res += str((x >> i) & 1)
    else:
      res += mask[len(mask) - 1 - i]
  
  return res

for line in lines:
  if line.startswith("mask"):
    mask = line.split()[-1]
  else:
    a, b = [int(x) for x in re.findall("\d+", line)]
    mem[a] = f(b)

print(sum(int(v, base=2) for v in mem.values()))
