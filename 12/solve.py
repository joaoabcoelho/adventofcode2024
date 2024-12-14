
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ list(line.rstrip()) for line in file]

nx = len(data[0])
ny = len(data[0])

sides = [(-1,0),(1,0),(0,1),(0,-1)]

def get_garden(p):
  garden = {p}
  l = data[p[1]][p[0]]
  def get_new_plots(garden):
    new_plots = []
    for g in garden:
      for s in sides:
        x = (g[0] + s[0], g[1] + s[1])
        if not 0 <= x[0] < nx: continue
        if not 0 <= x[1] < ny: continue
        if x in garden: continue
        if data[x[1]][x[0]] == l:
          new_plots.append(x)
    return new_plots
  done = False
  while not done:
    new_plots = get_new_plots(garden)
    for n in new_plots: garden.add(n)
    if len(new_plots)==0: done = True

  return garden

known_gardens = []

for x in range(nx):
  for y in range(ny):
    is_known = False
    for g in known_gardens:
      if (x,y) in g:
        is_known = True
        break
    if is_known: continue
    known_gardens.append(get_garden((x,y)))

def get_perimeter(p):
  l = data[p[1]][p[0]]
  ptr = 4
  for s in sides:
    x = (p[0] + s[0], p[1] + s[1])
    if not 0 <= x[0] < nx: continue
    if not 0 <= x[1] < ny: continue
    if data[x[1]][x[0]] == l: ptr -= 1

  return ptr

def get_vertices(p, g):
  corners = [(-1,-1), (-1,1), (1,-1), (1,1)]
  vertices = set()
  for c in corners:
    plots = [(p[0]+c[0], p[1]+c[1]),
             (p[0]+c[0], p[1]),
             (p[0], p[1]+c[1])]
    
    if (plots[1] not in g and plots[2] not in g) or \
       (plots[1] in g and plots[2] in g and plots[0] not in g):
      n = 1
      if plots[0] in g: n = 2
      vertices.add((2*p[0]+c[0], 2*p[1]+c[1], n))

  return vertices

#==============================================================================

def part1():

  total = 0

  for g in known_gardens:
    ptr = 0
    area = 0
    for p in g:
      ptr += get_perimeter(p)
      area += 1
    total += ptr * area


  print("Part 1:", total)


#==============================================================================

def part2():

  total = 0

  for g in known_gardens:
    vertices = set()
    for p in g:
      vertices.update(get_vertices(p, g))

    n = 0
    for v in vertices: n += v[2]
    total += len(g) * n

  print("Part 2:", total)

#==============================================================================

part1()
part2()
