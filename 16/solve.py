
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

moves = {(0,-1): '^', (0,1): 'v', (-1,0): '<', (1,0): '>'}

def dist_to_end(p):
  return abs(p[0]-end[0]) + abs(p[1]-end[1])

def propagate(head, dir):

  dirs = [dir, (dir[1], dir[0]), (-dir[1],-dir[0])]
  opts = []
  for d in dirs:
    if data[head[2][1]+d[1]][head[2][0]+d[0]] in ['.', 'E']: opts.append(d)
  if len(opts) != 1: return head

  pos = (head[2][0]+opts[0][0], head[2][1]+opts[0][1])
  cost = head[1] + 1
  if opts[0] != dir: cost += 1000
  path = head[4] + [(pos, moves[opts[0]])]
  head = (cost + dist_to_end(pos), cost, pos, opts[0], path)

  if pos==end: return head
  
  return propagate(head, opts[0])

def get_options(head):
  dir = head[3]
  dirs = [dir, (dir[1], dir[0]), (-dir[1],-dir[0])]
  opts = []
  for d in dirs:
    pos = (head[2][0]+d[0], head[2][1]+d[1])
    if data[pos[1]][pos[0]] not in ['.', 'E']: continue
    cost = head[1] + 1
    if d != head[3]: cost += 1000
    path = head[4] + [(pos, moves[d])]
    nh = propagate((cost + dist_to_end(pos), cost, pos, d, path), d)
    is_visited = False
    for h in head[4]:
      if nh[2] == h[0]:
        is_visited = True
        break
    if is_visited: continue
    opts.append(nh)

  return opts

def print_maze(head):

  subs = { p[0]: p[1] for p in head[-1]}
  subs.pop(end, None)
  for y in range(ny):
    for x in range(nx):
      print(subs.get((x,y), data[y][x]), end='')
    print()
      

def solve(part):

  heap = [(dist_to_end(start), 0, start, (1,0), [])]
  heapq.heapify(heap)

  best = {}
  sit = set()
  best_cost = 1e6
  
  total = 0

  while heap:

    head = heapq.heappop(heap)
    if head[2:4] in best:
      if head[0] <= best[head[2:4]]: best[head[2:4]] = head[0]
      else: continue
    else:
      best[head[2:4]] = head[0]
    if head[2] == end and head[0] <= best_cost:
      best_cost = head[0]
      total = head[0]
      for h in head[4]: sit.add(h[0])
      if part==1: break
    else:
      opts = get_options(head)
      for o in opts: heapq.heappush(heap, o)

  if part==1: return total
  else: return len(sit)+1

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
