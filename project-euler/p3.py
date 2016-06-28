#!/usr/bin/env python

"""Problem 3

Print greatest prime that divides n.

IDEA: 
Divide initial n by i = 1,2,... and keep n=n/i if divisible by
i. Divide by i repeatedly until new n no more divisible by
i. Resulting variable max is going to be a prime in the end because we
divide by each i until n is no more divisible by this i. Hence we are
"sieving" in a way.

"""

n = 600851475143

max = 0
i=2;
while(n>1):
    if(n%i == 0):
        if(max < i):
            max = i
        n = n/i # integer because n%i==0
    else:
        i += 1

print max 
