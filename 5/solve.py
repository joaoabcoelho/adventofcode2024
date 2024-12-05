
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [line.rstrip() for line in file]

deps = [ d for d in data if '|' in d ]
upds = [ d for d in data if ',' in d ]

graph = {}

for d in deps:
  v, k = d.split('|')
  if int(k) not in graph: graph[int(k)] = {int(v)}
  else: graph[int(k)].add(int(v))

def has_dep(x, l):
  for p in l:
    if p in graph.get(x, {}): return True
  return False

def is_valid(pages):
  for k in range(len(pages)):
    if has_dep(pages[k], pages[k+1:]): return False
  return True

#==============================================================================

def part1():

  total = 0

  for u in upds:
    pages = [ int(x) for x in u.split(',') ]
    if is_valid(pages):
      total += pages[int(len(pages)/2)]

  print("Part 1:", total)


#==============================================================================

def part2():

  total = 0

  for u in upds:
    pages = [ int(x) for x in u.split(',') ]
    if is_valid(pages): continue
    valid = []
    for i in range(len(pages)):
      for k in range(len(pages)):
        if not has_dep(pages[k], pages[:k] + pages[k+1:]):
          valid.append(pages[k])
          pages = pages[:k] + pages[k+1:]
          break
    total += valid[int(len(valid)/2)]

  print("Part 2:", total)

#==============================================================================

part1()
part2()
