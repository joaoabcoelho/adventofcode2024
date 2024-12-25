import sys, copy

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ line.rstrip() for line in file]

values = {}
gates = []
for d in data:
  if ':' in d:
    k,v = d.split(': ')
    values[k] = int(v)
  if ' -> ' in d:
    k1, op, k2 = d.split(' -> ')[0].split()
    rt = d.split(' -> ')[1]
    gates.append((k1,k2,op,rt))

def apply(val, gate):
  v1 = val[gate[0]]
  v2 = val[gate[1]]
  if gate[2]=='AND': return v1 and v2
  if gate[2]=='OR': return v1 or v2
  return v1 ^ v2

def compute(values, gates):
  val = copy.deepcopy(values)
  gat = copy.deepcopy(gates)
  while gat:
    g = gat.pop()
    if g[0] in val and g[1] in val:
      val[g[3]] = apply(val, g)
    else:
      gat.insert(0, g)
  return sum( v * 2**int(z[1:]) for z,v in val.items() if z.startswith('z') )

#==============================================================================

def part1():
  print("Part 1:", compute(values, gates))

#==============================================================================

def get_values(x,y):
  vals = { 'x{:02}'.format(k): int(v) 
           for k,v in enumerate('{:045b}'.format(x)[::-1]) }
  vals = vals | { 'y{:02}'.format(k): int(v) 
                  for k,v in enumerate('{:045b}'.format(y)[::-1]) }
  return vals

def part2():
  total = 0
  # Check wrong bits and examine adder gates manually
  for k in range(45):
    vxor = get_values(2**k,0)
    vand = get_values(2**k,2**k)
    zxor = compute(vxor, gates)
    zand = compute(vand, gates)
    if zxor != 2**k: print(k, 'xor', bin(zxor))
    if zand != 2**(k+1): print(k, 'and', bin(zand))
  print("Part 2:", ','.join(sorted(["mvb","z08","wss","z18",
                                    "z23","bmn","rds","jss"])))

#==============================================================================

part1()
part2()
