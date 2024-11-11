import random, NateUtils
NateUtils.print_slow("Game Start.")
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
    random.shuffle(rounds)
    
