import sys
from collections import defaultdict

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

seen = defaultdict(set)

for line in lines:
  ingredients, allergies = line.split("(contains ")
  ingredients = ingredients.split()
  allergies = allergies[:-1].split(", ")

  ingredients = frozenset(ingredients)

  for allergy in allergies:
    if allergy not in seen:
      seen[allergy] = set(ingredients)
    else:
      seen[allergy] = seen[allergy].intersection(ingredients)

done = set()

while True:
  x = None

  for v in seen.values():
    if len(v) == 1 and v.copy().pop() not in done:
      x = v.copy().pop()
      break

  if not x:
    break

  for v in seen.values():
    if len(v) != 1 and x in v:
      v.remove(x)

  done.add(x)

seen = [(k, v.pop()) for k, v in seen.items()]

seen.sort()

print(",".join(v[1] for v in seen))
