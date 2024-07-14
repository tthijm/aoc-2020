import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

FIELDS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
lines.append("")

res = 0
i = 0
fields = FIELDS.copy()

while i < len(lines):
  line = lines[i]
  i += 1

  if line == "":
    if not fields:
      res += 1
    
    fields = FIELDS.copy()
  else:
    remove = set()

    for v in fields:
      if v in line:
        remove.add(v)

    fields -= remove

print(res)
