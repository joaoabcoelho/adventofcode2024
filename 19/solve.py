
import sys
from functools import lru_cache

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ line.rstrip() for line in file]

patts = data[0].split(', ')
dsgns = data[2:]

def split(d):
  return [(p, d[len(p):]) for p in patts if d.startswith(p)]

@lru_cache(None)
def get_opts(d):
  if not d:
    return 1
  return sum(get_opts(o[1]) for o in split(d))

#==============================================================================

def part1():
  total = sum(1 for d in dsgns if get_opts(d))
  print("Part 1:", total)

#==============================================================================

def part2():
  total = sum(get_opts(d) for d in dsgns)
  print("Part 2:", total)

#==============================================================================

part1()
part2()
