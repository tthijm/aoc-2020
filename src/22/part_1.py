import sys
from collections import deque

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

m = lines.index("")
one = deque(int(x) for x in lines[1:m])
two = deque(int(x) for x in lines[m+2:])

while one and two:
  a, b = one.popleft(), two.popleft()

  if a > b:
    one.append(a)
    one.append(b)
  else:
    two.append(b)
    two.append(a)

res = 0

for i, v in enumerate(reversed(one if one else two)):
  res += (i + 1) * v

print(res)
