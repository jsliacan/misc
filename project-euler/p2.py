#!/usr/bin/env python

a = 1
b = 2
s = 0

while b < 4000000:
    if b%2 == 0:
        s += b
        
    c = b
    b = a+b
    a = c

print s
