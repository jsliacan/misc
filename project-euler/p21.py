#!/usr/bin/env python

#Problem 21

import math
from collections import Counter

amitable = [[0,0],[1,1]]

def factorize(n):

    pf = []
    cands = [p for p in primes if p<n+1]

    for c in cands:
        while n>1 and n%c == 0:
            n = n/c
            pf.append(c) # just a few times so dont care

    return pf
        

def sum_divisors(n):

    l = factorize(n)
    ctr = Counter(l).items()
    divisors = [1]
    for p,m in ctr:
        newdivisors = []
        for j in range(1,m+1):
            newdivisors.extend([d*(p**j) for d in divisors])
        divisors.extend(newdivisors)
    return sum(divisors[:-1])


#start = time.time()

primes = []
N = 1000 
L = range(N+1) 
for n in L:
    if n > 1:
        primes.append(n) # not many primes, so not slow
        for i in range(1,int(math.ceil(N/n))+1):
            L[n*i] = 0


for n in range(2,10000):
    amitable.append([n,sum_divisors(n)])

s = 0
for item in amitable:
    a,b = item
    if b<10000 and amitable[a] == amitable[b][::-1] and a<b:
            s += (a+b)

print s
