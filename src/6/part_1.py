import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines.append("")

res = 0
seen = set()

i = 0

while i < len(lines):
  line = lines[i]

  if not line:
    res += len(seen)
    seen = set()
  else:
    for c in line:
      seen.add(c)

  i += 1

print(res)
