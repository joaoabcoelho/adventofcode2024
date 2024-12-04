import sys
import numpy as np
from collections import Counter

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [line.rstrip().split() for line in file]

data = np.array(data).astype(int)

#==============================================================================

def part1():

  l1 = sorted(data[:,0])
  l2 = sorted(data[:,1])

  s = 0

  for n1, n2 in zip(l1,l2):

    s += abs(n1-n2)

  print("Part 1:", s)

#==============================================================================

def part2():

  c = Counter(data[:,1])

  s = 0

  for d in data[:,0]:
    s += d * c[d]

  print("Part 2:", s)

#==============================================================================

part1()
part2()
