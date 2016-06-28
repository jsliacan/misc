#!/usr/bin/env python

"""
Problem 5

IDEA:
create list: [2,3,4,...,20]
then go from left to right and sieve in a funny way -- when at element
i in the list, divide each number to the right of i in the list by i
if divisible, otherwise don't touch. At the end, multiply all numbers
in the modified list.
"""
r = range(2,21)

index_i = 0
for i in r:
    index_j = 0
    for j in r[(index_i+1):]:
        if j%i==0:
            r[index_i+1+index_j] = j/i

        index_j += 1
    index_i += 1

lcm = 1
for i in r:
    lcm *= i

print lcm
