#!/usr/bin/env python

N = 2000000
numbers = range(N)
s = 0
for n in numbers:
    if n>1 and n != 0:
        for j in range(2*n, N, n):
            if j%n==0: numbers[j] = 0
        s += n

print s
