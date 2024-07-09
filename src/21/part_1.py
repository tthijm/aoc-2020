import sys
from collections import defaultdict

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

seen = defaultdict(frozenset)

for line in lines:
  ingredients, allergies = line.split("(contains ")
  ingredients = ingredients.split()
  allergies = allergies[:-1].split(", ")

  ingredients = frozenset(ingredients)

  for allergy in allergies:
    if allergy not in seen:
      seen[allergy] = ingredients
    else:
      seen[allergy] = seen[allergy].intersection(ingredients)

without = set()

for s in seen.values():
  without = without.union(s)

res = 0

for line in lines:
  ingredients = line.split("(contains ")[0].split()

  for x in ingredients:
    if x not in without:
      res += 1

print(res)
