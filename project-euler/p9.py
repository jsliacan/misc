#!/usr/bin/env python

"""
c = sqrt(a^2 + b^2)
a+b = 1000 - c = 1000 - sqrt(a^2 + b^2) 
then:
b = (1000^2 - 2000a)/(2000 - 2a)
a<b<c
a+b+c = 1000
a,b,c integers
"""
import math

for a in range(1000):
    b = (1000*1000-(2000*a))/(2000-2*a)
    if b > a:
        c = math.sqrt(a*a + b*b)
        if c > b:
            if float(b).is_integer() and c.is_integer() and a+b+c==1000:
                print int(a*b*c)
