
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ list(line.rstrip()) for line in file]

data = [ int(d) for d in data[0] ]

#==============================================================================

def part1():

  id = 0
  is_file = True
  disk = []

  for d in data:
    if is_file:
      disk += [id]*d
      id += 1
    else:
      disk += [-1]*d
    is_file = not is_file

  f = 0
  b = len(disk)-1

  while f<b:
    if disk[f] > -1:
      f += 1
      continue
    if disk[b] < 0:
      b -= 1
      continue
    disk[f] = disk[b]
    disk[b] = -1
    f += 1
    b -= 1

  total = 0

  for i in range(len(disk)):
    if disk[i] < 0: break
    total += i * disk[i]

  print("Part 1:", total)


#==============================================================================

def part2():

  files = []
  spaces = []
  id = 0
  pos = 0
  is_file = True
  for d in data:
    if is_file:
      files.append([id, pos, d])
      id += 1
    else:
      spaces.append([pos, d])
    pos += d
    is_file = not is_file

  for k in range(len(files)-1,-1,-1):
    for i in range(len(spaces)):
      if files[k][2] <= spaces[i][1] and \
         files[k][1] > spaces[i][0]:
        files[k][1] = spaces[i][0]
        spaces[i][0] += files[k][2]
        spaces[i][1] -= files[k][2]
        break

  total = 0
  for f in files:
    for i in range(f[2]):
      total += f[0] * (f[1] + i)

  print("Part 2:", total)

#==============================================================================

part1()
part2()
