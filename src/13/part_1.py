import sys, re

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

start = int(lines[0])
best = (start + 1000, -1)
busses = [int(x) for x in re.findall("\d+", lines[1])]

for bus in busses:
  wait = 0 if start % bus == 0 else start + (bus - (start % bus))

  if wait < best[0]:
    best = (wait, bus * (wait - start))

print(best[1])
