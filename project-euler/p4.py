#!/usr/bin/env python 

"""Problem 4

IDEA:
Go through 3digit numbers from largest to smallest and multiply
them. If resulting number palindromic, compare to the max. Return max.

"""


max = 0

for i in range(999,99,-1):
    for j in range(i,99,-1):
        n = i*j
        strn = str(n)
        if(strn == strn[::-1] and n > max):
            max = n


print max
    
