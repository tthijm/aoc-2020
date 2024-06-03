import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

def f():
  acc = 0
  i = 0
  j = 0

  while i < len(lines) and j < 500:
    line = lines[i].split()
    instruction = line[0]
    n = int(line[1])

    if instruction == "acc":
      acc += n
      i += 1
    elif instruction == "jmp":
      i += n
    else:
      i += 1

    j += 1

  return acc if i == len(lines) else None

for i in range(len(lines)):
  line = lines[i]
  split = line.split()

  if split[0] == "nop":
    lines[i] = f"jmp {split[1]}"
  elif split[0] == "jmp":
    lines[i] = f"nop {split[1]}"
  
  x = f()

  if x:
    print(x)
    break

  lines[i] = line
