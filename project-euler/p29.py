#!/usr/bin/env python

from collections import Counter
# Problem 29

# plain brute force :(

n = 100

distinct_powers = set()

for a in range(2,n+1):
    for b in range(2,n+1):
        distinct_powers.add(a**b)

print len(distinct_powers)
