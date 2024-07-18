import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

cups = [None] * 1000001

for i in range(len(lines[0]) - 1):
  current = int(lines[0][i])
  next = int(lines[0][i + 1])

  cups[current] = next

cups[int(lines[0][-1])] = len(lines[0]) + 1

for i in range(len(lines[0]) + 1, 1000000):
  cups[i] = i + 1

cups[-1] = int(lines[0][0])

current = int(lines[0][0])

for _ in range(10000000):
  destination = current

  while destination in [current, cups[current], cups[cups[current]], cups[cups[cups[current]]]]:
    destination = destination - 1 if destination != 1 else 1000000

  current_next = cups[cups[cups[cups[current]]]]
  destination_next = cups[current]
  picked_next = cups[destination]

  cups[cups[cups[cups[current]]]] = picked_next
  cups[current] = current_next
  cups[destination] = destination_next

  current = cups[current]

print(cups[1] * cups[cups[1]])
