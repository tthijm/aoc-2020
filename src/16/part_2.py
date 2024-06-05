import sys, re

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

ranges = []

for line in lines[:lines.index("")]:
  nums = [int(x) for x in re.findall("\d+", line)]

  ranges.append(nums)

tickets = []

for line in lines[lines.index("nearby tickets:") + 1:]:
  v = True

  for x in line.split(","):
    x = int(x)
    valid = False

    for r in ranges:
      if r[0] <= x <= r[1] or r[2] <= x <= r[3]:
        valid = True
        break
    
    if not valid:
      v = False
      break

  if v:
    tickets.append(line)

options = [set(i for i in range(lines.index(""))) for _ in range(lines.index(""))]

for ticket in tickets:
  ticket = [int(x) for x in ticket.split(",")]

  for i in range(len(ticket)):
    for j in range(len(options)):
      r = ranges[j]

      if not (r[0] <= ticket[i] <= r[1] or r[2] <= ticket[i] <= r[3]):
        if j in options[i]:
          options[i].remove(j)

def solve():
  seen = set()
  done = False

  while not done:
    done = True

    for option in options:
      if len(option) == 1:
        v = option.copy().pop()

        if v not in seen:
          seen.add(v)
          done = False

          for option in options:
            if len(option) > 1 and v in option:
              option.remove(v)

solve()

options = [option.pop() for option in options]
ticket = [int(x) for x in lines[lines.index("your ticket:") + 1].split(",")]
res = 1

for i in range(len(options)):
  if options[i] <= 5:
    res *= ticket[i]

print(res)
