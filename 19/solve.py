
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ line.rstrip() for line in file]

patts = data[0].split(', ')
dsgns = data[2:]

def split(d):

  opts = []
  for p in patts:
    if p == d[:len(p)]:
      opts.append([p, d[len(p):]])

  return opts

cache = {}
def get_opts(d):

  if not d: return 1
  if d in cache: return cache[d]

  opts = split(d)
  out = 0
  for o in opts:
    out += get_opts(o[1])

  cache[d] = out

  return out

#==============================================================================

def part1():
  total = 0
  for d in dsgns:
    if get_opts(d): total+=1
  print("Part 1:", total)

#==============================================================================

def part2():
  total = 0
  for d in dsgns:
    total += get_opts(d)
  print("Part 2:", total)

#==============================================================================

part1()
part2()
