
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ line.rstrip().split() for line in file]

data = [ int(d) for d in data[0] ]

cache = {}

def split(s):

    if s==0: return [1]
    elif len(str(s))%2==0:
      st = str(s)
      n = len(st)
      return [int(st[:n//2]), int(st[n//2:])]
    else: return [s * 2024]

def blink(stone, n):

  if n==0: return 1

  if (stone, n) in cache:
    return cache[(stone, n)]

  stones = split(stone)

  total = 0
  for s in stones:
    total += blink(s, n-1)

  cache[(stone, n)] = total
  return total

#==============================================================================

def part1():

  total = 0

  for s in data:
    total += blink(s, 25)

  print("Part 1:", total)


#==============================================================================

def part2():

  total = 0

  for s in data:
    total += blink(s, 75)

  print("Part 2:", total)

#==============================================================================

part1()
part2()
