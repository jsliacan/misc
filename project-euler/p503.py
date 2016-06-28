#!/usr/bin/env python
from __future__ import division

import math

# Problem 503

n = 10 #n = 4
N = (n-1)*(int(n*(n+1)/2)) # N = 30
M = n*(n-1) # M = 12
Ewait = N/M # Ewait = 5/2

print "n=",n
print "N=",N
print "M=",M
print "Ewait=",Ewait

score = 0

norm = 1
for c in range(2,n):

    norm *= 1/c
    m = math.floor(2*N/(c*(c+1)))
    p = int(math.ceil(c/2))+1
    for k in range(1,p):
        #print norm,"*(",k*m,"/",int(M/c),")"
        score += norm*(k*m/(M/c))

    if c == n-1:
        for k in range(p,c+1):
            #print norm,"*",Ewait
            score += norm*Ewait
            #print score

print score
