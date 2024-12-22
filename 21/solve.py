
import sys, heapq
from functools import lru_cache

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

def move(state, button, level):
  key = state[level]
  isnum = level == len(state)-1
  pos = numpad[key] if isnum else movpad[key]
  dpos = moves[button]
  pos = (pos[0]+dpos[0], pos[1]+dpos[1])
  key = padnum.get(pos,'') if isnum else padmov.get(pos,"")
  return state[:level] + (key,) + state[level+1:]

def robot(state, button):

  if button!='A': return move(state, button, 0)

  next_move = 0
  while next_move < len(state)-1 and state[next_move] == 'A': next_move += 1
  if next_move==len(state)-1: return state

  return move(state, state[next_move], next_move+1)

def is_valid(state):
  for s in state:
    if s=='': return False
  return True

def get_neighbors(state, visited):

  buttons = ['<','^','v','>','A']
  neighbors = []
  for b in buttons:
    n = robot(state, b)
    if n in visited: continue
    if not is_valid(n): continue
    neighbors.append(n)

  return neighbors

def solve(start, end, nrobots):

  total = 0
  start = tuple(['A']*nrobots + [start])
  end = tuple(['A']*nrobots + [end])
  visited = {start}
  heap = [(0, start)]
  heapq.heapify(heap)

  while heap:
    test = heapq.heappop(heap)
    if test[1] == end:
      total = test[0]
      break

    neighbors = get_neighbors(test[1], visited)

    for n in neighbors:
      heapq.heappush(heap, (test[0]+1, n))
      visited.add(n)

  return total+1

def get_length(d, nrobots):
  return sum( solve(d[(k-1)%len(d)], d[k], nrobots) for k in range(len(d)) )

def get_score(d, nrobots):
  value = int(d[:-1])
  length = get_length(d, nrobots)
  return value * length

#==============================================================================

def part1():
  total = sum( get_score(d, 2) for d in data )
  print("Part 1:", total)

#==============================================================================

def part2():
  total = sum( get_score(d, 5) for d in data )
  print("Part 2:", total, "for 5 robots")

#==============================================================================

part1()
part2()
