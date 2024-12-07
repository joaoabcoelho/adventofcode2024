
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [line.rstrip().split() for line in file]

def combi(c, x, r, is_part2):

  nc = [ ci * x for ci in c ] + \
       [ ci + x for ci in c ]

  if is_part2: nc += [ int(str(ci) + str(x)) for ci in c ]

  nc = [ x for x in nc if x <= r ]

  return nc

def get_total(is_part2):

  total = 0

  for d in data:

    r = int(d[0].split(':')[0])
    c = [int(d[1])]
    for x in d[2:]:
      c = combi(c, int(x), r, is_part2)
    for ci in c:
      if ci==r:
        total += r 
        break

  return total

#==============================================================================

def part1():

  total = get_total(False)

  print("Part 1:", total)


#==============================================================================

def part2():

  total = get_total(True)

  print("Part 2:", total)

#==============================================================================

part1()
part2()
