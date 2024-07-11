import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

card, door = (int(x) for x in lines)

loops = 1
value = 7

while value != card:
  value *= 7
  value %= 20201227
  loops += 1

value = door

for _ in range(loops - 1):
  value *= door
  value %= 20201227

print(value)
