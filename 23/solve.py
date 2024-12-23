import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ line.rstrip().split('-') for line in file]

connections = {}
for d in data:
  connections[d[0]] = connections.get(d[0],[]) + [d[1]]
  connections[d[1]] = connections.get(d[1],[]) + [d[0]]

def has_t(s):
  for x in s:
    if x.startswith('t'): return True
  return False

#==============================================================================

def part1():
  threesomes = set()
  for k,v in connections.items():
    n = len(v)
    if n<2: continue
    for i in range(n):
      for j in range(i+1,n):
        if v[i] in connections[v[j]]:
          s = [k,v[i],v[j]]
          if not has_t(s): continue
          threesomes.add(tuple(sorted(s)))
  print("Part 1:", len(threesomes))

#==============================================================================

def part2():
  total = 0
  print("Part 2:", total)

#==============================================================================

part1()
part2()
