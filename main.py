import random, NateUtils
NateUtils.print_slow("Game Start.")

def toshootornottoshoot(that_is="the question"):
  global rounds
  return sum(rounds)/len(rounds)

while True:
  rounds = []
  live_num = 0
  blank_num = 0
  for i in range(random.randint(1,10)):
    rounds += [1]
    live_num += 1
  toprint = str(live_num) + " Live."
  NateUtils.print_slow(toprint)
  for i in range(random.randint(1,10)):
    rounds += [0]
    live_num += 0
  toprint = str(live_num) + " Blank."
  NateUtils.print_slow(toprint)  
  NateUtils.print_slow("I insert the shells in an unknown order.")
  random.shuffle(rounds)
  phealth = 3
  dhealth = 3
  NateUtils.print_slow("We each have three blood transfusions")
  while True:
    NateUtils.print_slow("Begin.")
