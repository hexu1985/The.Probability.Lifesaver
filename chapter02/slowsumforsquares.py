#!/usr/bin/env python3

import sys
import math

def slowsumforsquares(m, print_result):
    result_list = []
    count = 0
    for a in range(0, int(math.sqrt(m))+1):
        for b in range(0, a+1):
            for c in range(0, b+1):
                for d in range(0, c+1):
                    if a**2 + b**2 + c**2 + d**2 == m:
                        count = count + 1
                        result_list.append((a, b, c, d))
    print("The number of representations of {} as a sum of four squares with a >= b >= c >= d is {} .".format(m, count))
    if print_result:
        print(result_list)

if __name__ == "__main__":
    m = 2000
    if len(sys.argv) > 1:
        m = int(sys.argv[1])

    slowsumforsquares(m, True)


