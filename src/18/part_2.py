import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

res = 0

def f(line, i):
  if line[i + 2] != "(":
    return i + 2
  else:
    s = 1
    i += 3

    while s:
      if line[i] == "(":
        s += 1
      elif line[i] == ")":
        s -= 1

      i += 1

    return i - 1

def g(line, i):
  if line[i - 2] != ")":
    return i - 2
  else:
    s = -1
    i -= 3

    while s:
      if line[i] == "(":
        s += 1
      elif line[i] == ")":
        s -= 1

      i -= 1

    return i + 1

for line in lines:
  line = [c for c in line]

  start = 0

  while "+" in line[start:]:

    part = line[start:]

    i = part.index("+")
    left = g(line, start + i)
    right = f(line, start + i)

    line[left:right + 1] = ["("] + line[left:right + 1] + [")"]

    start += i + 2

  res += eval("".join(line))

print(res)
