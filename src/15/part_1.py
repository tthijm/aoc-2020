import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

nums = [int(x) for x in lines[0].split(",")]
seen = collections.defaultdict(list)
last = nums[-1]

for i, num in enumerate(nums):
  seen[num] = [i]

for i in range(len(nums), 2020):
  if len(seen[last]) == 1:
    last = 0
    seen[0].append(i)
  else:
    a, b = seen[last][-2], seen[last][-1]
    last = b - a
    seen[last].append(i)

print(last)
