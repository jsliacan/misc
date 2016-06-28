#!/usr/bin/env python

# runs in ~0.12s

import math, time
from collections import Counter

def factorize(n):

    pf = []
    cands = [p for p in primes if p<n+1]

    for c in cands:
        while n>1 and n%c == 0:
            n = n/c
            pf.append(c) # just a few times so dont care
            
    return pf
        

def num_divisors(t):

    n1,n2 = t[0],t[1]
    l1,l2 = [],[]

    if n1%2 == 0:
        l1 = factorize(n1/2)
        l2 = factorize(n2)
    else:
        l1 = factorize(n1)
        l2 = factorize(n2/2)

    num_divisors = 1
    for i in Counter(l1+l2).items():
        num_divisors *= (i[1]+1)

    return num_divisors


#start = time.time()

primes = []
N = 20 # ~9 primes should suffice
L = range(N+1) 
for n in L:
    if n > 1:
        primes.append(n) # not many primes, so not slow
        for i in range(1,int(math.ceil(N/n))+1):
            L[n*i] = 0

r = 1
while r > 0:
    nd = num_divisors((r,r+1))
    if nd > 499:
        print r*(r+1)/2, nd
        break
    r +=1

#end = time.time()
#print end-start
