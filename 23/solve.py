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

def connects_all(s, o):
  for x in s:
    if o not in connections[x]: return False
  return True

def get_next(lower):
  higher = set()
  for s in lower:
    options = connections[s[0]]
    for o in options:
      if connects_all(s, o):
        higher.add(tuple(sorted(list(s)+[o])))
  return higher

#==============================================================================

def part1():
  total = sum( 1 for s in get_next(data) if has_t(s) )
  print("Part 1:", total)

#==============================================================================

def part2():
  sets = data
  while True:
    print(str(len(list(sets)[0]))+'-somes:', len(sets))
    next = get_next(sets)
    if len(next)==0: break
    sets = next
  print("Part 2:", ','.join(list(sets)[0]))

#==============================================================================

part1()
part2()
