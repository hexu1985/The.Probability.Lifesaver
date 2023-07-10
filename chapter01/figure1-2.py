#!/usr/bin/env

noshare = [(1, 1)]
share = [(1, 0)]
currentnoshare = 1
for n in range(2, 51):
    newfactor = (365 - (n-1))/365
    currentnoshare = currentnoshare * newfactor
    noshare.append((n, currentnoshare))
    share.append((n, 1.0 - currentnoshare))

print("share:", share)
print("noshare:", noshare)
