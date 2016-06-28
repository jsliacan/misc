#!/usr/bin/env python

# runs in ~11s

import time

def len_colatz(n):
    # recurse, just for fun
    if n > 1 and n%2==0: return 1+len_colatz(n/2)
    elif n > 1: return 1+len_colatz(3*n+1)
    else: return 0

s = time.time()

# below could be simpler, but this speeds it up:
# simplify check of doubles of previous numbers

mx_colatz = 0
mx_n = 2
N = 1000000
L = range(2,N)
for n in L:
    if n > 0:
        nlen = len_colatz(n)
        k = 0
        while n*(2**k) < N-2:
            L[n*(2**k)] = 0
            k += 1
        if mx_colatz < nlen+k-1:
            mx_colatz = nlen+k-1
            mx_n = n*(2**(k-1))

e = time.time()

print mx_n, "[elapsed time:", e-s,"secs]"
