
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [line.rstrip() for line in file]

nx = len(data[0])
ny = len(data)

dir = '^'
px = 0
py = 0

for y in range(ny):
  data[y] = list(data[y])

for y in range(ny):
  px = "".join(data[y]).find(dir)
  if px != -1:
    py = y
    data[py][px] = 'X'
    break

dirs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

px0, py0, dir0 = px, py, dir
visited = set()

def evolve():

  global px, py, dir, visited

  npx = px + dirs[dir][0]
  npy = py + dirs[dir][1]

  if (not 0 <= npx < nx) or \
     (not 0 <= npy < ny):
     return 1

  if (px, py, dir) in visited:
    return 2

  visited.add((px, py, dir))

  if data[npy][npx] != '#':
    px = npx
    py = npy
    data[npy][npx] = 'X'
  else:
    dir = turn[dir]

  return 0

#==============================================================================

def part1():

  total = 0

  while evolve() == 0: continue

  for d in data:
    for c in d:
      if c == 'X': total += 1

  print("Part 1:", total)


#==============================================================================

def part2():

  global px, py, dir, visited

  total = 0

  path = set()
  for x in range(nx):
    for y in range(ny):
      if data[y][x] == 'X': path.add((x,y))

  for x in range(nx):
    print('.', end='', flush=True)
    for y in range(ny):
      if data[y][x] == '#': continue
      if (x, y) == (px0, py0): continue
      if (x, y) not in path: continue
      data[y][x] = '#'
      px, py, dir = px0, py0, dir0
      visited = set()
      r = 0
      while r == 0: r = evolve()
      if r == 2: total += 1
      data[y][x] = '.'

  print("\nPart 2:", total)

#==============================================================================

part1()
part2()
