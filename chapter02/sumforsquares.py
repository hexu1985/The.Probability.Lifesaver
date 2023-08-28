#!/usr/bin/env python3

import sys
import math

def slowsumforsquares(m, print_result):
    result_list = []
    count = 0
    for a in range(0, int(math.sqrt(m))+1):
        for b in range(0, int(min(a, math.sqrt(m-a**2)))+1):
            for c in range(0, int(min(b, math.sqrt(m-a**2-b**2)))+1):
                d_square = m - a**2 - b**2 - c**2
                if d_square >= 0:
                    d = math.sqrt(d_square)
                    if d <= c and int(d) == d:
                        count = count + 1
                        result_list.append((a, b, c, int(d)))

    print("The number of representations of {} as a sum of four squares with a >= b >= c >= d is {} .".format(m, count))
    if print_result:
        print(result_list)

if __name__ == "__main__":
    m = 2000
    if len(sys.argv) > 1:
        m = int(sys.argv[1])

    slowsumforsquares(m, True)


