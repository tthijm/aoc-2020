import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = [int(x) for x in lines]

seen = set(lines[:25])

for num in lines[25:]:
  found = False

  for a in seen:
    for b in seen:
      if a + b == num:
        found = True
        break
    
    if found:
      break
  
  if not found:
    print(num)
    break

  seen.add(num)
