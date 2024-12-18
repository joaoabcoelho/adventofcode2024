
import sys, heapq

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ tuple([ int(i) for i in line.rstrip().split(',')]) for line in file]

is_test = filename=='test.txt'
end = (6,6) if is_test else (70,70)

def get_neighbors(p, blocked, visited):

  dirs = [(-1,0),(1,0),(0,-1),(0,1)]
  neighbors = []
  for d in dirs:
    n = (p[0]+d[0], p[1]+d[1])
    if not 0 <= n[0] <= end[0]: continue
    if not 0 <= n[1] <= end[1]: continue
    if n in visited: continue
    if n in blocked: continue
    neighbors.append(n)

  return neighbors

def solve(nbytes):

  total = 0
  visited = {(0,0)}
  blocked = set(data[:nbytes])
  heap = [(0, (0,0))]
  heapq.heapify(heap)

  while heap:
    test = heapq.heappop(heap)
    if test[1] == end:
      total = test[0]
      break

    neighbors = get_neighbors(test[1], blocked, visited)

    for n in neighbors:
      heapq.heappush(heap, (test[0]+1, n))
      visited.add(n)

  return total

#==============================================================================

def part1():
  total = solve(12 if is_test else 1024)
  print("Part 1:", total)

#==============================================================================

def part2():
  n = len(data)
  total = 0
  while total == 0:
    n -= 1
    total = solve(n)

  print("Part 2:", data[n])

#==============================================================================

part1()
part2()
