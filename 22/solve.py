import sys

filename = "input.txt"
if len(sys.argv)>1: filename = sys.argv[1]

with open(filename) as file:
  data = [ int(line.rstrip()) for line in file]

def get_next(x):
  x = ((64 * x) ^ x ) % 16777216
  x = ((x // 32) ^ x ) % 16777216
  return ((2048 * x) ^ x ) % 16777216
  
def evolve(x, n=2000):
  for k in range(n): x = get_next(x)
  return x

def get_seq(x, n=2000):
  prices = [x]
  for k in range(n):
    x = get_next(x)
    prices.append(x)

  prices = [ p%10 for p in prices ]

  changes = [ prices[k+1]-prices[k] for k in range(n) ]

  seqs = { tuple(changes[k:k+4]): prices[k+4] for k in range(n-4,-1,-1) }

  return seqs

#==============================================================================

def part1():
  total = sum( evolve(d) for d in data )
  print("Part 1:", total)

#==============================================================================

def part2():
  total = 0
  seqs = [ get_seq(d) for d in data ]
  best = {}
  for seq in seqs:
    for k,v in seq.items():
      if k in best: best[k] += v
      else: best[k] = v 
  best_value = 0
  best_seq = (0,0,0,0)
  for k,v in best.items():
    if v>best_value:
      best_value = v
      best_seq = k
  print("Part 2:", best_value)

#==============================================================================

part1()
part2()
