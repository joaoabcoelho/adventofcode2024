
import sys, copy

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ line.rstrip() for line in file]

register = {}
program = []
for d in data:
  if "Program" in d:
    program = [ int(x) for x in d.split(': ')[1].split(',') ]
    continue
  if not d: continue
  item = d.split(': ')
  value = int(item[1])
  key = item[0].split('Register ')[1]
  register[key] = value

defaultReg = { k: v for k,v in register.items() }

def combo(x):
  if x==4: return register['A']
  if x==5: return register['B']
  if x==6: return register['C']
  return x

output = []
pointer = 0

def adv(x):
  register['A'] = register['A'] // 2**combo(x)

def bxl(x):
  register['B'] = register['B'] ^ x

def bst(x):
  register['B'] = combo(x) % 8

def jnz(x):
  global pointer
  if register['A']: pointer = x - 2

def bxc(x):
  register['B'] = register['B'] ^ register['C']

def out(x):
  output.append(combo(x) % 8)

def bdv(x):
  register['B'] = register['A'] // 2**combo(x)

def cdv(x):
  register['C'] = register['A'] // 2**combo(x)

opcode = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

def run_program(reg):

  global pointer, output, register
  pointer = 0
  register = reg
  output = []
  c = 0
  while pointer < len(program) and c<100000:
    opcode[program[pointer]](program[pointer+1])
    c += 1
    pointer += 2
    #print(c, pointer, register, output)
  return output

def strlist(l):
  return ','.join([ str(v) for v in l ])

#==============================================================================

def part1():

  run_program(defaultReg)

  print("Part 1:", strlist(output))

#==============================================================================

def part2():
  possible = [0]
  for k in range(len(program)-1,-1,-1):
    update = []
    for p in possible:
      for i in range(8):
        myreg = copy.deepcopy(defaultReg)
        test = p + i * 8**k
        myreg['A'] = test
        run_program(myreg)
        if len(output)<k+1: continue
        if output[k] == program[k]: update.append(test)
    possible = update
  total = min(possible)
  print("Part 2:", total)

#==============================================================================

part1()
part2()
