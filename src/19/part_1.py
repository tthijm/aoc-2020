import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

rules = {}
m = lines.index("")

for i in range(m):
  line = lines[i].split(": ")
  i = int(line[0])

  if "a" in line[1] or "b" in line[1]:
    rules[i] = line[1][-2]
  else:
    rules[i] = [[int(x) for x in v.split()] for v in line[1].split(" | ")]

def f(j = 0):
  if isinstance(rules[j], str):
    return [rules[j]]
  else:
    options = []

    for path in rules[j]:
      option = [""]

      for step in path:
        new_option = []

        for v in f(step):
          for o in option:
            new_option.append(o + v)

        option = new_option

      options += option

    return options

valid = set(f())
res = 0

for line in lines[m + 1:]:
  if line in valid:
    res += 1

print(res)
