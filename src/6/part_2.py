import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines.append("")

res = 0
seen = set()
first = True

i = 0

while i < len(lines):
  line = lines[i]

  if not line:
    res += len(seen)
    seen = set()
    first = True
  else:
    if first:
      seen = set(line)
      first = False
    else:
      seen.intersection_update(set(line))

  i += 1

print(res)
