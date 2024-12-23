
import sys
from functools import cache
from itertools import permutations

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ line.rstrip() for line in file]

numpad = { str(k): ((k-1)%3, 2-((k-1)//3)) for k in range(1,10) }
numpad['A'] = (2,3)
numpad['0'] = (1,3)
padnum = {}
for k,v in numpad.items(): padnum[v] = k

movpad = {'^': (1,0), 'A': (2,0), '<': (0,1), 'v': (1,1), '>': (2,1)}
padmov = {}
for k,v in movpad.items(): padmov[v] = k

moves = {'^': (0,-1), 'v': (0,1), '<': (-1,0), '>': (1,0)}

def move(key, button, isnum):
  pos = numpad[key] if isnum else movpad[key]
  dpos = moves[button]
  pos = (pos[0]+dpos[0], pos[1]+dpos[1])
  key = padnum.get(pos,'') if isnum else padmov.get(pos,"")
  return key

def validpath(start, path, isnum):
  for p in path:
    start = move(start, p, isnum)
    if not start: return False
  return True
  
def minpath(start, end, isnum=True):
  p1 = numpad[start] if isnum else movpad[start]
  p2 = numpad[end] if isnum else movpad[end]
  dp = (p2[0]-p1[0], p2[1]-p1[1])
  path = abs(dp[0]) * ('<' if dp[0]<0 else '>') + \
         abs(dp[1]) * ('^' if dp[1]<0 else 'v')

  paths = set(permutations(path))
  
  paths = [ ''.join(p) + "A" for p in paths if validpath(start, p, isnum) ]

  return paths

@cache
def rsolve(start, end, nrobots, isnum):

  paths = minpath(start, end, isnum)

  if nrobots==0: return len(paths[0])

  values = [ sum( rsolve(p[(k-1)%len(p)], p[k], nrobots-1, False)
             for k in range(len(p)) ) for p in paths ]

  return min(values)

def get_sol(pin, n):
  total = 0
  for k in range(len(pin)):
    step = (pin[(k-1)%len(pin)], pin[k])
    total += rsolve(step[0], step[1], n, True)

  return total

def get_score(d, nrobots):
  value = int(d[:-1])
  length = get_sol(d, nrobots)
  return value * length

#==============================================================================

def part1():
  total = sum( get_score(d, 2) for d in data )
  print("Part 1:", total)

#==============================================================================

def part2():
  total = sum( get_score(d, 25) for d in data )
  print("Part 2:", total)

#==============================================================================

part1()
part2()
