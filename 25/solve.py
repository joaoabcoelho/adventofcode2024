import sys, copy

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ list(line.rstrip()) for line in file]

keys = []
locks = []
for k in range(0,len(data),8):
  obj = [5]*5
  for r in range(1,6):
    for c in range(5):
      if data[k+r][c] == '.': obj[c] -= 1
  if '.' in data[k]: keys.append(obj)
  else: locks.append(obj)

def fits(key, lock):
  for k in range(5):
    if key[k] + lock[k] > 5: return False
  return True

#==============================================================================

def part1():
  total = 0
  for k in keys:
    for l in locks:
      if fits(k,l): total += 1
  print("Part 1:", total)

#==============================================================================

def part2():
  total = 0
  print("Part 2:", total)

#==============================================================================

part1()
part2()
