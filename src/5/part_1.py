import sys, math

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

def f(line):
  low, high = 0, 127

  for c in line[:7]:
    if c == "F":
      high -= math.ceil((high - low) / 2)
    else:
      low += math.ceil((high - low) / 2)

  r = low
  low, high = 0, 7

  for c in line[-3:]:
    if c == "L":
      high -= math.ceil((high - low) / 2)
    else:
      low += math.ceil((high - low) / 2)

  return (r, low)

res = -1

for line in lines:
  r, c = f(line)

  res = max(res, r * 8 + c)

print(res)
