#!/usr/bin/env python3

import random

def diamonddraw(num):
    awin = 0
    bwin = 0
    cwin = 0
    for n in range(1, num+1):
        diamond = 0
        while diamond == 0:
            c1 = random.randint(1, 52)
            c2 = random.randint(1, 52)
            c3 = random.randint(1, 52)
            if c1 <= 13 or c2 <= 13 or c3 <= 13:
                diamond = 1
            if diamond == 1:
                if c1 <= 13:
                    awin = awin + 1
                elif c2 <= 13:
                    bwin = bwin + 1
                elif c3 <= 13:
                    cwin = cwin + 1

    print("Here are the observed probabilities from {} games.".format(num))
    print("Percent Alice won (approx): {}%.".format(100.0 * awin / num))
    print("Percent Bob won (approx): {}%.".format(100.0 * bwin / num))
    print("Percent Charlie won (approx): {}%.".format(100.0 * cwin / num))
    print("Predictions (from our bad logic) were approx {}% {}% {}%".format(1600.0/37, 4800.0/175, 900.0/37))

if __name__ == "__main__":
    diamonddraw(1000000)

