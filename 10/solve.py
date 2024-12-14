
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ list(line.rstrip()) for line in file]

data = [ [ int(c) for c in r ] for r in data ]

nx = len(data[0])
ny = len(data)

def step(p):

  n = data[p[1]][p[0]] + 1

  test = [(1,0), (-1,0), (0,1), (0,-1)]

  valid = []

  for t in test:
    x = (p[0]+t[0], p[1]+t[1])
    if not 0 <= x[0] < nx: continue
    if not 0 <= x[1] < ny: continue
    if data[x[1]][x[0]] == n: valid.append(x)

  return valid

#==============================================================================

def part1():

  total = 0

  heads = [ (x,y) for x in range(nx) for y in range(ny) if data[y][x]==0 ]

  for h in heads:
    current = {h}
    for s in range(9):
      next = set()
      for c in current:
        test = step(c)
        for t in test: next.add(t)
      current = next
    total += len(current)

  print("Part 1:", total)


#==============================================================================

def part2():

  total = 0

  heads = [ (x,y) for x in range(nx) for y in range(ny) if data[y][x]==0 ]

  for h in heads:
    current = {h}
    for s in range(9):
      next = []
      for c in current:
        test = step(c)
        for t in test: next.append(t)
      current = next
    total += len(current)

  print("Part 2:", total)

#==============================================================================

part1()
part2()
