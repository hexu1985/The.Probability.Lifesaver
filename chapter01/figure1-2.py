#!/usr/bin/env python3

import matplotlib.pyplot as plt

noshare = [(1, 1)]
share = [(1, 0)]
currentnoshare = 1
for n in range(2, 51):
    newfactor = (365 - (n-1))/365
    currentnoshare = currentnoshare * newfactor
    noshare.append((n, currentnoshare))
    share.append((n, 1.0 - currentnoshare))

#print("share:", share)
#print("noshare:", noshare)

N, P = zip(*share)
#print(N, P)
plt.scatter(N, P)

plt.xlabel("n")
plt.ylabel("probability")

plt.minorticks_on()

plt.show()
