#!/usr/bin/env python

# Problem 66

# won't work -- too slow!

from __future__ import division
from math import sqrt

"""
since (x-1)(x+1) = x^2-1
we have
"""

Dmax = 1000
Xmax = 0
dmax = 0
for d in range(2,Dmax+1):
    if sqrt(d).is_integer():
        continue
    print d
    y = 1
    x = sqrt(d*(y**2)+1)
    while not x.is_integer():
        y += 1
        x = sqrt(d*(y**2)+1)
    if x > Xmax:
        Xmax = int(x)
        dmax = d
print Xmax
