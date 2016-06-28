#!/usr/bin/env python

"""
Problem 7

IDEA: 
Keep track of primes so far. Always try to divide new number by
primes in the list (from smallest to largest for efficiency). If not
divisible by any, it is new prime. Add to the list. Keep going until
list has length 10001. Then return last element.

Runtime: 
real	0m4.743s
user	0m4.730s
sys	0m0.011s
"""


num_primes = 1;
primes = [2]
n = 3
while(num_primes < 10001):

    is_prime = True
    for p in primes:
        if n%p == 0:
            is_prime = False
            break

    if is_prime == True:
        primes.append(n)
        num_primes += 1
                
    n += 1

print primes[-1]
