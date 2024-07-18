import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

cups = list(int(x) for x in lines[0])
current = cups[0]

for _ in range(100):
  index = cups.index(current)
  a, b, c = (cups[(index + 1 + j) % len(cups)] for j in range(3))
  destination = current

  while destination in [current, a, b, c]:
    destination = ((destination - 2) % 9) + 1

  cups = cups[max(index - 5, 0):index + 1] + cups[index + 4:]
  cups = cups[:cups.index(destination) + 1] + [a, b, c] + cups[cups.index(destination) + 1:]

  current = cups[(cups.index(current) + 1) % len(cups)]

print("".join(str(x) for x in cups[cups.index(1) + 1:] + cups[:cups.index(1)]))
