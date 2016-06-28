#!/usr/bin/env python

"""
Problem 6

IDEA:
(\sum_i i)^2 = (\sum_i i^2) + 2*(\sum_{i<j} i*j)
Hence: (\sum_i i)^2 - (\sum_i i^2) = 2*(\sum_{i<j} i*j).
So compute only: 2*(\sum_{i<j} i*j).
"""


sum = 0
for i in range(1,101):
    for j in range(1,i):
        sum += (2*i*j)

print sum
