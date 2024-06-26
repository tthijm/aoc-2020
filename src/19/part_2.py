import sys, collections

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

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

def f(line):
  q = collections.deque([(0, 0, [])])

  while q:
    i, j, s = q.popleft()

    if i == len(line) and not s:
      return True

    if i + len(s) >= len(line) or j == -1:
      continue

    if isinstance(rules[j], str):
      if line[i] == rules[j]:
        q.append((i + 1, s.pop() if s else -1, s))
    else:
      for option in rules[j]:
        q.append((i, option[0], s + option[1:][::-1]))

  return False

res = 0

for line in lines[m + 1:]:
  if f(line):
    res += 1

print(res)
