import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [line.rstrip().split() for line in file]

def is_safe(l):
  x0 = int(l[0])
  x1 = int(l[1])
  if x1>x0:
    xmin = 1
    xmax = 3
  else:
    xmin = -3
    xmax = -1
  for k in range(1,len(l)):
    if not xmin <= int(l[k]) - int(l[k-1]) <= xmax:
      return 0, k

  return 1, len(l)

#==============================================================================

def part1():

  s = 0

  for l in data:
    s += is_safe(l)[0]

  print("Part 1:", s)

#==============================================================================

def part2():

  s = 0

  for l in data:
    g, k = is_safe(l)
    if g==1:
      s += 1
    else:
      r = [0, k-1, k]
      for ri in r:
        li = l[:ri] + l[ri+1:]
        gi, ki = is_safe(li)
        if gi==1:
          s += 1
          break

  print("Part 2:", s)

#==============================================================================

part1()
part2()
