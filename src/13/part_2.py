import sys, sympy.ntheory.modular

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

m = []
v = []

for i, x in enumerate(lines[1].split(",")):
  if x != "x":
    v.append(i)
    m.append(int(x))

x = sympy.ntheory.modular.crt(m, v)
print(x[1] - x[0])
