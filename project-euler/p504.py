#!/usr/bin/env python

# Problem 504
# ~10s
# fifi's idea to have triangle lookup table: 35s --> 31s speedup (compared to gcd lookup table that I had before)
# improved symmetry checking after that, gives 10s runtime

from __future__ import division
import time
from collections import Counter
from math import sqrt

m = 100

def gcd(x,y):
    if x < y:
        swap = y
        y = x
        x = swap
    if y == 0: return x
    else: return gcd(y, x%y)

trian_table = [[((x+1)*(y+1)-2*(x+y)-(gcd(x,y)-1))//2 for x in range(1,m+1)] for y in range(1,m+1)]

def num_pts(p,q,r,t):
    return trian_table[p-1][q-1] + trian_table[q-1][r-1] + trian_table[t-1][r-1] + trian_table[t-1][p-1] + p+q+r+t-3

t = time.time()
num_squares = 0
for a in range(1,m+1):
    for b in range(a,m+1):
        for c in range(b,m+1):
            for d in range(c,m+1):

                n = num_pts(a,b,c,d)
                is_int = sqrt(n).is_integer()

                # aaaa
                if a==d:
                    if is_int: num_squares+=1

                # aaad/abbb
                elif a==c or b==d:
                    if is_int: num_squares+=4  

                # aacc
                elif a==b and c==d:
                    if is_int: num_squares+=4
                    n = num_pts(a,c,b,d)
                    if sqrt(n).is_integer(): num_squares+=2

                # aacd/abbd/abcc
                elif a==b or b==c or c==d:
                    if is_int: num_squares+=8
                    if a==b:
                        n = num_pts(a,c,b,d) # acad
                        if sqrt(n).is_integer(): num_squares+=4
                    if b==c:
                        n = num_pts(a,b,d,b) # abdb
                        if sqrt(n).is_integer(): num_squares+=4
                    if c==d:
                        n = num_pts(a,c,b,d) # acbc
                        if sqrt(n).is_integer(): num_squares+=4
                # abcd
                else: 
                    if is_int: num_squares+=8
                    n = num_pts(a,c,b,d) # acbd
                    if sqrt(n).is_integer(): num_squares+=8
                    n = num_pts(a,b,d,c) # abdc
                    if sqrt(n).is_integer(): num_squares+=8

print num_squares, time.time()-t,"sec"
