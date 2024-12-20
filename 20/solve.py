import sys
from functools import lru_cache

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ list(line.rstrip()) for line in file]

nx = len(data[0])
ny = len(data)

track = []
for x in range(nx):
  for y in range(ny):
    if data[y][x] == 'S':
      track.append((x,y))
      break

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

while data[track[-1][1]][track[-1][0]]!='E':
  h = track[-1]
  for d in dirs:
    n = (h[0]+d[0], h[1]+d[1])
    if not 0 <= n[0] < nx: continue
    if not 0 <= n[1] < ny: continue
    if data[n[1]][n[0]] in ['.','E'] and (len(track)==1 or n!=track[-2]):
      track.append(n)
      break

def solve(ps, minsave):
  total = 0
  nt = len(track)
  for i in range(nt-minsave-2):
    for j in range(i+minsave+2,nt):
      dist = abs(track[i][0]-track[j][0]) + abs(track[i][1]-track[j][1])
      if dist>ps: continue
      if j-i-dist<minsave: continue
      total += 1
  return total

#==============================================================================

def part1():
  print("Part 1:", solve(2, 100))

#==============================================================================

def part2():
  print("Part 2:", solve(20, 100))

#==============================================================================

part1()
part2()
