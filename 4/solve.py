
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [line.rstrip() for line in file]

nr = len(data)
nc = len(data[0])

#==============================================================================

def part1():

  word = "XMAS"

  total = 0

  for r in range(nr):
    for c in range(nc):
      if data[r][c] != word[0]: continue
      dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
      for d in dirs:
        is_xmas = True
        for k in range(1,len(word)):
          rk = r + k * d[0]
          ck = c + k * d[1]
          if (not 0 <= rk < nr) or \
             (not 0 <= ck < nc) or \
             (data[rk][ck] != word[k]):
            is_xmas = False
            break
        if is_xmas: total += 1


  print("Part 1:", total)


#==============================================================================

def part2():

  word = "MAS"

  total = 0

  for r in range(nr):
    for c in range(nc):
      if data[r][c] != word[1]: continue
      dirs = [(1,1), (-1,-1), (1,-1), (-1,1)]
      nd = 0
      for d in dirs:
        is_xmas = True
        for k in range(-1,2):
          rk = r + k * d[0]
          ck = c + k * d[1]
          if (not 0 <= rk < nr) or \
             (not 0 <= ck < nc) or \
             (data[rk][ck] != word[k+1]):
            is_xmas = False
            break
        if is_xmas: nd += 1
      if nd==2: total += 1


  print("Part 2:", total)

#==============================================================================

part1()
part2()
