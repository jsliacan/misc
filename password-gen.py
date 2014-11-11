#!/usr/bin/env python


import random


basestr = "abcdefghijkllmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUWXYZ0123456789"

N = 12
pswd = ""
L = len(basestr)

for i in range(N):
    pswd += basestr[int(random.uniform(0,L-1))]

print pswd
