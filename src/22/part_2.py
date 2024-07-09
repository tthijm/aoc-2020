import sys
from collections import deque

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

m = lines.index("")
one = deque(int(x) for x in lines[1:m])
two = deque(int(x) for x in lines[m+2:])

def score(x):
  total = 0

  for i, v in enumerate(reversed(x)):
    total += (i + 1) * v

  return total

def f(left, right):
  seen = set()

  while left and right:
    scores = (score(left), score(right))

    if scores in seen:
      return True

    a, b = left.popleft(), right.popleft()

    if a <= len(left) and b <= len(right):
      if f(deque(list(left)[:a]), deque(list(right)[:b])):
        left.append(a)
        left.append(b)
      else:
        right.append(b)
        right.append(a)
    else:
      if a > b:
        left.append(a)
        left.append(b)
      else:
        right.append(b)
        right.append(a)

    seen.add(scores)

  return True if left else False

f(one, two)
print(score(one) + score(two))
