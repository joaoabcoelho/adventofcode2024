
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ line.rstrip() for line in file]

puzzles = []

for k in range(0, len(data), 4):
  puzzle = {}
  puzzle["AX"] = int(data[k].split('X+')[1].split(',')[0])
  puzzle["AY"] = int(data[k].split('Y+')[1].split(',')[0])
  puzzle["BX"] = int(data[k+1].split('X+')[1].split(',')[0])
  puzzle["BY"] = int(data[k+1].split('Y+')[1].split(',')[0])
  puzzle["X"] = int(data[k+2].split('X=')[1].split(',')[0])
  puzzle["Y"] = int(data[k+2].split('Y=')[1].split(',')[0])
  puzzle["X2"] = int(data[k+2].split('X=')[1].split(',')[0]) + 10000000000000
  puzzle["Y2"] = int(data[k+2].split('Y=')[1].split(',')[0]) + 10000000000000
  puzzles.append(puzzle)

#==============================================================================

def part1():

  total = 0

  for p in puzzles:

    ra = (p["BY"] * p["X"] - p["BX"] * p["Y"]) % \
         (p["BY"] * p["AX"] - p["BX"] * p["AY"])

    rb = (p["AY"] * p["X"] - p["AX"] * p["Y"]) % \
         (p["AY"] * p["BX"] - p["AX"] * p["BY"])

    if ra==0 and rb==0:
      a = (p["BY"] * p["X"] - p["BX"] * p["Y"]) // \
          (p["BY"] * p["AX"] - p["BX"] * p["AY"])

      b = (p["AY"] * p["X"] - p["AX"] * p["Y"]) // \
          (p["AY"] * p["BX"] - p["AX"] * p["BY"])

      total += 3*a + b

  print("Part 1:", total)


#==============================================================================

def part2():

  total = 0

  for p in puzzles:

    ra = (p["BY"] * p["X2"] - p["BX"] * p["Y2"]) % \
         (p["BY"] * p["AX"] - p["BX"] * p["AY"])

    rb = (p["AY"] * p["X2"] - p["AX"] * p["Y2"]) % \
         (p["AY"] * p["BX"] - p["AX"] * p["BY"])

    if ra==0 and rb==0:
      a = (p["BY"] * p["X2"] - p["BX"] * p["Y2"]) // \
          (p["BY"] * p["AX"] - p["BX"] * p["AY"])

      b = (p["AY"] * p["X2"] - p["AX"] * p["Y2"]) // \
          (p["AY"] * p["BX"] - p["AX"] * p["BY"])

      total += 3*a + b

  print("Part 2:", total)

#==============================================================================

part1()
part2()
