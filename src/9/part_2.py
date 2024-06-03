import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

TARGET = 552655238
lines = [int(x) for x in lines]

left = 0
total = 0

for right in range(len(lines)):
  total += lines[right]

  while total > TARGET:
    total -= lines[left]
    left += 1

  if total == TARGET and left != right:
    x = lines[left:right + 1]
    print(min(x) + max(x))
    break
