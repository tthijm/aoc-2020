import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

res = 0

for line in lines:
  s = []

  for c in line.replace(" ", ""):
    if c.isdigit():
      c = int(c)

      if not s or s[-1] == "(":
        s.append(c)
      else:
        op = s.pop()

        if op == "*":
          s.append(s.pop() * c)
        else:
          assert op == "+"
          s.append(s.pop() + c)
    else:
      if c == ")":
        b = s.pop()
        assert s.pop() == "("

        if len(s) > 1 and s[-1] != "(":
          op, a = s.pop(), s.pop()

          if op == "*":
            s.append(a * b)
          else:
            assert op == "+"
            s.append(a + b)
        else:
          s.append(b)
      else:
        s.append(c)

  assert len(s) == 1

  res += s.pop()

print(res)
