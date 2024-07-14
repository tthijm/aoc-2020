import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

FIELDS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
lines.append("")

res = 0
i = 0
fields = FIELDS.copy()
valid = True

def f(k, v):
  match k:
    case "byr":
      return 1920 <= int(v) <= 2002
    case "iyr":
      return 2010 <= int(v) <= 2020
    case "eyr":
      return 2020 <= int(v) <= 2030
    case "hgt":
      if "cm" in v:
        return 150 <= int(v.replace("cm", "")) <= 193
      else:
        return 59 <= int(v.replace("in", "")) <= 76
    case "hcl":
      return len(v) == 7 and all(ord("0") <= ord(x) <= ord("9") or ord("a") <= ord(x) <= ord("f") for x in v[1:])
    case "ecl":
      return v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    case "pid":
      return len(v) == 9 and v.isnumeric()
    case "cid":
      return True

  assert False

while i < len(lines):
  line = lines[i]
  i += 1

  if line == "":
    if not fields and valid:
      res += 1

    fields = FIELDS.copy()
    valid = True
  elif valid:
    for x in line.split():
      k, v = x.split(":")

      if not f(k, v):
        valid = False
        break

      if k != "cid":
        fields.remove(k)

print(res)
