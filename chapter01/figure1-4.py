#!/usr/bin/env python3

import math
import random
import numpy
import matplotlib.pyplot as plt

def cal_theorybdaylist(days, max):
    noshare = [1]*(max+1)
    share = [0]*(max+1)
    for k in range(2, max+1):
        noshare[k] = noshare[k-1] * (1 - (k-1)/365)
        share[k] = 1.0 - noshare[k]
    return share

def birthdaycdf(num, days):
    numpeople = [0]*(days+1)

    for n in range(1, num+1):
        share = False
        bdaylist = []
        k = 0
        while not share:
            x = random.randint(1, days)
            if x not in bdaylist:
                bdaylist.append(x)
            else:
                share = True

            k = k + 1

            if share:
                for d in range(k, days+1):
                    numpeople[d] += 1

    bdaylistplot = []
    max = int(3 * (0.5 + math.sqrt(days*math.log(4))))
    print("max:", max)
    for d in range(1, max+1):
        bdaylistplot.append((d, numpeople[d]*1.0/num))
    print(bdaylistplot)

    print("n is", int(0.5 + math.sqrt(days*math.log(4))))
    print("Observed probability of success with 1/2 + sqrt[D log(4)] people is",
            numpeople[int(0.5 + math.sqrt(days*math.log(4)))]*100.0/num, "%.")

    f = cal_theorybdaylist(max=max, days=days)
    theorybdaylistplot = []
    for d in range(1, max+1):
        theorybdaylistplot.append((d, f[d])) 
    print(theorybdaylistplot)

    
    N, P = zip(*bdaylistplot)
    p1 = plt.scatter(N, P, marker='+')
    
    N, P = zip(*theorybdaylistplot)
    p2 = plt.scatter(N, P, marker='^', alpha=0.5)
    
    plt.legend([p1, p2], ["experiment", "theory"])
    
    plt.xlabel("n")
    plt.ylabel("Prob")
    
    plt.minorticks_on()

    plt.show()


if __name__ == "__main__":
    birthdaycdf(20000, 365)
