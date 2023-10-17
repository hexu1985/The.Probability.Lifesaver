#!/usr/bin/env python3

import sys
import random

def onepair(numdo):
    count = 0
    deck = []
    # for i in [1, 13]
    for i in range(1, 13+1):
        # for j in [1, 4]
        for j in range(1, 4+1):
            deck.append(i)

    card = [0]*(13+1)
    for n in range(1, numdo+1):
        for i in range(0, 13+1):
            card[i] = 0
        hand = random.sample(deck, 5)
        for k, _ in enumerate(hand):
            card[hand[k]] = 1
        if sum(card) == 4:
            count += 1

    print("Theory says probability one pair is {}%.".format(352/8.33))
    print("Observed probability is {}%.".format(100*count/numdo))

if __name__ == "__main__":
    n = 10000000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])

    onepair(n)

