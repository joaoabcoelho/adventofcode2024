import sys, re

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [line.rstrip() for line in file]

#==============================================================================

def part1():

  total = 0

  for line in data:

    muls = re.findall("mul\([0-9]+,[0-9]+\)", line)

    for m in muls:
      n = m.split('(')[1].split(')')[0].split(',')
      if int(n[0])<1000 and int(n[1])<1000: total += int(n[0]) * int(n[1])

  print("Part 1:", total)


#==============================================================================

def part2():

  total = 0

  enabled = True

  for line in data:

    muls = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)

    for m in muls:
      if m=="do()":
        enabled = True
        continue
      if m=="don't()":
        enabled = False
        continue
      if not enabled: continue
      n = m.split('(')[1].split(')')[0].split(',')
      if int(n[0])<1000 and int(n[1])<1000: total += int(n[0]) * int(n[1])

  print("Part 2:", total)

#==============================================================================

part1()
part2()
