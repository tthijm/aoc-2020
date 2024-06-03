import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

acc = 0
i = 0
seen = set()

while i not in seen:
  line = lines[i].split()
  instruction = line[0]
  n = int(line[1])

  seen.add(i)

  if instruction == "acc":
    acc += n
    i += 1
  elif instruction == "jmp":
    i += n
  else:
    i += 1

print(acc)
