
import sys, heapq

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ list(line.rstrip()) for line in file]

nx = len(data[0])
ny = len(data)

start = (0,0)
end = (0,0)
for x in range(nx):
  for y in range(ny):
    if data[y][x] == 'S': start = (x,y)
    if data[y][x] == 'E': end = (x,y)

def get_options(head):
  dir = head[2]
  dirs = [dir, (dir[1], dir[0]), (-dir[1],-dir[0])]
  opts = []
  for d in dirs:
    pos = (head[1][0]+d[0], head[1][1]+d[1])
    if pos in head[3]: continue
    if data[pos[1]][pos[0]] not in ['.', 'E']: continue
    cost = head[0] + 1
    if d != head[2]: cost += 1000
    opts.append((cost, pos, d, head[3].union({pos})))

  return opts

def solve(part):

  heap = [(0, start, (1,0), {start})]
  heapq.heapify(heap)

  best = {}
  sit = set()
  best_cost = 1e6
  
  total = 0

  while heap:
    head = heapq.heappop(heap)
    if head[1:3] in best:
      if head[0] <= best[head[1:3]]: best[head[1:3]] = head[0]
      else: continue
    else:
      best[head[1:3]] = head[0]
    if head[1] == end and head[0] <= best_cost:
      best_cost = head[0]
      total = head[0]
      if part==1: break
      sit.update(head[3])
    else:
      opts = get_options(head)
      for o in opts: heapq.heappush(heap, o)

  if part==1: return total
  else: return len(sit)

#==============================================================================

def part1():
  total = solve(1)
  print("Part 1:", total)

#==============================================================================

def part2():
  total = solve(2)
  print("Part 2:", total)

#==============================================================================

part1()
part2()
