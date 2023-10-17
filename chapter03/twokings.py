#!/usr/bin/env python3

import sys
import random

def twokings(numdo):
    count = 0
    deck = [1]*4
    for i in range(5, 52+1):
        deck.append(0)

    for n in range(1, numdo+1):
        hand = random.sample(deck, 5)
        if sum(hand) == 2:
            count += 1
    
    print("Probability of exactly 2 kings is {}%.".format(2162/541.45))
    print("Observed probability is {}%.".format(100*count/numdo))

if __name__ == "__main__":
    n = 10000000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])

    twokings(n)




