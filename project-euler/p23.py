#!/usr/bin/env python

#Problem 23

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
M = 28123 # all ints greater than this can be written as sum of two abundants

primes = []
N = M+1
L = range(N+1) 
for n in L:
    if n > 1:
        primes.append(n) # not many primes, so not slow
        for i in range(1,int(math.ceil(N/n))+1):
            L[n*i] = 0




# find abundant numbers < M+1
A = []
for a in range(12,M+1):
    if sum_divisors(a) > a:
        A.append(a)

soa = [0 for x in range(M+1)]
n = len(A)
for i in range(n):
    for j in range(n):
        if i+j<M+1:
            soa[i+j] = 1

print M+1-sum(soa)
