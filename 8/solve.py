
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ list(line.rstrip()) for line in file]

nx = len(data[0])
ny = len(data)

freq = {}

for x in range(nx):
  for y in range(ny):
    c = data[y][x]
    if c == '.': continue
    if c not in freq: freq[c] = [(x,y)]
    else: freq[c].append((x,y))

def is_bound(a):
  if not 0 <= a[0] < nx: return False
  if not 0 <= a[1] < ny: return False
  return True

#==============================================================================

def part1():

  antinodes = set()

  for v in freq.values():
    for i in range(len(v)):
      for j in range(i+1, len(v)):
        a1 = (2*v[i][0] - v[j][0], 2*v[i][1] - v[j][1])
        a2 = (2*v[j][0] - v[i][0], 2*v[j][1] - v[i][1])
        if is_bound(a1): antinodes.add(a1)
        if is_bound(a2): antinodes.add(a2)

  total = len(antinodes)

  print("Part 1:", total)


#==============================================================================

def part2():

  antinodes = set()

  for v in freq.values():
    for i in range(len(v)):
      for j in range(i+1, len(v)):
        dx = (v[i][0] - v[j][0], v[i][1] - v[j][1])
        maxk = max(nx, ny)
        for k in range(-maxk, maxk+1):
          a = (v[i][0] + k * dx[0], v[i][1] + k * dx[1])
          if is_bound(a): antinodes.add(a)

  total = len(antinodes)

  print("Part 2:", total)

#==============================================================================

part1()
part2()
