#!/usr/bin/env python

import time
from math import factorial

"""
Solution (takes ~0.07s)

Use 2 facts: 

1. numbers with permuted digits have the
same end of the sequence (check only these numbers in the lookup table
and multiply by number of permutations -- do not forget to include
leading zeros!)

2. sum of squares of digits is up to 567 (create lookup table)

"""

def seq(n):
    while (n != 1 and n != 89): n = sqs(n)
    return 1-n%89 # 1 if n==89 and 0 if n==1

def sqs(n):
    s = 0
    while n > 0:
        a = n%10
        n = n/10
        s += a*a
    return s

def mapfactorial(l):
    p = 1
    for i in l:
        p *= factorial(i)
    return p

def mult(n):
    # super important to count leading zeros!!! AAAAARGH
    l = [0 for x in range(10)]
    j = 0
    while n > 0:
        a = n%10
        n = n/10
        l[a] += 1
        j+=1
    l[0] = 7-j

    return 5040/mapfactorial(l)

if __name__ == "__main__":


    t = time.time()
    
    N = 81*7
    L = [0 for x in range(N+1)]
    
    for i in range(2,N+1): L[i] = seq(i)


    i = 0
    counter = 0
    for a in range(10):
        for b in range(a,10):
            for c in range(b,10):
                for d in range(c,10):
                    for e in range(d,10):
                        for f in range(e,10):
                            for g in range(f,10):
                                k = a*10**6 + b*10**5 + c*10**4 + d*10**3 + e*100 + f*10 + g
                                n = sqs(k)
                                counter += L[n]*mult(k)
                                i += 1
                                
    print counter, time.time()-t,"sec"





""" -------------------------------------------------------------------------------
Brute-force solution! (takes ~80s)

"""
 

"""
t = time.time()
N = 10000000
numbers = [x for x in range(1,N)]
classification = [0 for x  in range(1,N)]

def makeloop(n):
    m = n
    lst = []
    while (m != 89) and (m != 1):
        if m < n:
            m = classification[m-1]
            break
        elif m > n-1:
            lst.append(m)
        m = sum([int(x)*int(x) for x in str(m)])

    for i in lst:
        if i-1<N-1:
            classification[i-1] = m

    return m == 89

counter = 0
for n in numbers:
    if classification[n-1] == 89:
        counter += 1
    elif classification[n-1] == 0:
        if makeloop(n): counter += 1
    else:
        continue

print counter
print time.time()-t
"""
