"""
IDEA: there are 9! permutations starting with 0, same number
starting with 1. Our permutation must start with 2, since
3*(9!)>999999. Proceed similarly for each digit.
"""
def fac(n):
    """factorial function"""
    if n == 0:
        return 1
    else:
        return n*fac(n-1)
    

N = 999999 # this many numbers before 1000000th perm
l = range(10)
f = [0 for x in range(10)]

for i in range(9,-1,-1):
    faci = fac(i)
    d = int(float(N)/faci)
    N = N-(d*faci)
    f[9-i]=l.pop(d)

print f
