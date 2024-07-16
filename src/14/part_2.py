import sys, collections, re

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

mem = collections.defaultdict(int)
mask = None

def insert(x, value):
  q = collections.deque([""])

  for i in range(len(mask)):
    for _ in range(len(q)):
      v = q.popleft()

      if mask[i] == "1":
        q.append(v + "1")
      elif mask[i] == "0":
        q.append(v + str((x >> (len(mask) - 1 - i)) & 1))
      else:
        assert mask[i] == "X"
        q.append(v + "1")
        q.append(v + "0")

  for v in q:
    mem[v] = value

for line in lines:
  if line.startswith("mask"):
    mask = line.split()[-1]
  else:
    insert(*[int(x) for x in re.findall("\d+", line)])

print(sum(v for v in mem.values()))
