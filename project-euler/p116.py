#!/usr/bin/env python

# Problem 116

from math import factorial as f

def bin(n,k): return f(n)//(f(k)*f(n-k))
    
N = 50
L = [2,3,4]
num_ways = 0

for l in L:
    for i in range(1,N//l+1):
        num_ways += bin(N-i*l+i,i)

print num_ways
