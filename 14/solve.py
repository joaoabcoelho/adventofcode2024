
import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

nx = 101
ny = 103
if filename=="test.txt":
  nx = 11
  ny = 7

with open(filename) as file:
  data = [ line.rstrip() for line in file]

robots = []

for k in range(len(data)):
  robot = {}
  robot["x"] = int(data[k].split('p=')[1].split(',')[0])
  robot["y"] = int(data[k].split('p=')[1].split(',')[1].split()[0])
  robot["vx"] = int(data[k].split('v=')[1].split(',')[0])
  robot["vy"] = int(data[k].split('v=')[1].split(',')[1])
  robots.append(robot)

def run_robot(r, n):
  px = (r['x'] + n * r['vx']) % nx
  py = (r['y'] + n * r['vy']) % ny
  return px, py

#==============================================================================

def part1():

  quads = [0, 0, 0, 0]

  for r in robots:
    px, py = run_robot(r, 100)
    mx = nx // 2
    my = ny // 2
    if px < mx and py < my: quads[0] += 1
    elif px < mx and py > my: quads[1] += 1
    elif px > mx and py < my: quads[2] += 1
    elif px > mx and py > my: quads[3] += 1

  total = quads[0] * quads[1] * quads[2] * quads[3]

  print("Part 1:", total)


#==============================================================================

def print_robots(robs):

  img = [ [ '.' for x in range(nx) ] for y in range(ny) ]
  for r in robs:
    img[r[1]][r[0]] = 'o'

  for row in img:
    print(''.join(row))

def check_robots(robs):

  robset = set(robs)
  for r in robset:
    n = 0
    for dx in range(-1,2):
      for dy in range(-1,2):
        if (r[0]+dx, r[1]+dy) in robset: n += 1
    if n == 9: return True

  return False

def part2():

  total = 0

  for n in range(10000):
    robs = [ run_robot(r, n) for r in robots ]
    if check_robots(robs):
      print('='*40,n,'='*40)
      print_robots(robs)
      total = n
      break

  print("Part 2:", total)

#==============================================================================

part1()
part2()
