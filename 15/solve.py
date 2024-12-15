
import sys, copy

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ list(line.rstrip()) for line in file]

room = [ d for d in data if '#' in d ]

moves = [ ]
for d in data:
  if '#' not in d: moves += d 

move_dict = {'>': (1,0), '<': (-1,0), 'v': (0,1), '^': (0,-1)}

def get_robot(room):
  nx = len(room[0])
  ny = len(room)

  robot = (0,0)
  for x in range(nx):
    found = False
    for y in range(ny):
      if room[y][x] == '@':
        robot = (x,y)
        found = True
        break
    if found: break

  return robot

def move(room, robot, m):

  dx = move_dict[m]
  p = (robot[0]+dx[0], robot[1]+dx[1])

  if room[p[1]][p[0]] == '#':
    return room, robot

  if room[p[1]][p[0]] == '.':
    room[robot[1]][robot[0]] = '.'
    robot = p
    room[p[1]][p[0]] = '@'
    return room, robot

  b = p
  while room[b[1]][b[0]] == 'O':
    b = (b[0]+dx[0], b[1]+dx[1])

  if room[b[1]][b[0]] == '#':
    return room, robot

  room[robot[1]][robot[0]] = '.'
  robot = p
  room[p[1]][p[0]] = '@'
  room[b[1]][b[0]] = 'O'
  return room, robot
  

def print_room(room):
  for r in room: print(''.join(r))

def gps(room):
  nx = len(room[0])
  ny = len(room)
  total = 0
  for x in range(nx):
    for y in range(ny):
      if room[y][x] in ['O', '[']:
        total += 100*y + x
  return total
  
#==============================================================================

def part1(room):

  robot = get_robot(room)

  for m in moves:
    room, robot = move(room, robot, m)

  total = gps(room)

  print("Part 1:", total)


#==============================================================================

room2 = []
for r in room:
  row = []
  for c in r:
    if c == '#': row += ['#', '#']
    if c == '.': row += ['.', '.']
    if c == '@': row += ['@', '.']
    if c == 'O': row += ['[', ']']
  room2.append(row)

def push_box(room, p, m):

  if room[p[1]][p[0]] != '[':
    return room, False

  dx = move_dict[m]

  if m == '<' or m == '>':
    if room[p[1]][p[0]+(1+3*dx[0])//2] == '#':
      return room, False
    elif room[p[1]][p[0]+(1+3*dx[0])//2] == '.':
      room[p[1]][p[0]+dx[0]] = '['
      room[p[1]][p[0]+dx[0]+1] = ']'
      room[p[1]][p[0]+(1-dx[0])//2] = '.'
      return room, True
    else:
      room, moved = push_box(room, (p[0]+2*dx[0], p[1]), m)
      if moved: return push_box(room, p, m)
      else: return room, False

  if m == 'v' or m == '^':
    if room[p[1]+dx[1]][p[0]] == '#' or room[p[1]+dx[1]][p[0]+1] == '#':
      return room, False
    elif room[p[1]+dx[1]][p[0]] == '.' and room[p[1]+dx[1]][p[0]+1] == '.':
      room[p[1]+dx[1]][p[0]] = '['
      room[p[1]+dx[1]][p[0]+1] = ']'
      room[p[1]][p[0]] = '.'
      room[p[1]][p[0]+1] = '.'
      return room, True
    elif room[p[1]+dx[1]][p[0]] != ']' or room[p[1]+dx[1]][p[0]+1] != '[':
      bx = p[0]
      if room[p[1]+dx[1]][p[0]] == ']': bx -= 1
      if room[p[1]+dx[1]][p[0]] == '.': bx += 1
      room, moved = push_box(room, (bx, p[1]+dx[1]), m)
      if moved: return push_box(room, p, m)
      else: return room, False
    else:
      room_before = copy.deepcopy(room)
      room, moved = push_box(room, (p[0]-1, p[1]+dx[1]), m)
      if moved:
        room, moved = push_box(room, (p[0]+1, p[1]+dx[1]), m)
        if moved: return push_box(room, p, m)
        else: return room_before, False
      else: return room_before, False


def move2(room, robot, m):

  dx = move_dict[m]
  p = (robot[0]+dx[0], robot[1]+dx[1])

  if room[p[1]][p[0]] == '#':
    return room, robot

  if room[p[1]][p[0]] == '.':
    room[robot[1]][robot[0]] = '.'
    robot = p
    room[p[1]][p[0]] = '@'
    return room, robot

  moved = False
  if room[p[1]][p[0]] == '[':
    room, moved = push_box(room, p, m)
  elif room[p[1]][p[0]] == ']':
    room, moved = push_box(room, (p[0]-1,p[1]), m)

  if moved:
    room, robot = move2(room, robot, m)
      
  return room, robot


def part2(room):

  robot = get_robot(room)

  for m in moves:
    room, robot = move2(room, robot, m)

  total = gps(room)

  print("Part 2:", total)

#==============================================================================

part1(room)
part2(room2)
