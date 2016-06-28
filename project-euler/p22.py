#!/usr/bin/env python

# Problem 22

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = len(alphabet)

f = open("data22.txt", "r")
names = f.readline().split('","')
names[0] = names[0][1:] # split doesn't get rid of the first ", so this needed
names.sort() # trivial in python...
N = len(names)

name_vals = [0 for x in range(N)]

for i in range(n):
    l = alphabet[i]
    for j in range(N):
        for c in names[j]:
            if c == l: name_vals[j] += (i+1)


for i in range(N):
    name_vals[i] *=(i+1)

print sum(name_vals)
