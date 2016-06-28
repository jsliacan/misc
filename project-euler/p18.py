#!/usr/bin/env python

# runs instantly

N = 17 # keep extra column on left and right
T = [[0 for x in range(N)] for y in range(N)]
f = open("data18.txt", "r")

# save in T
i = 0
for line in f:
    row = line.split()
    for j in range(1,len(row)+1):
        T[i][j] = int(row[j-1])
    i += 1

# overwrite values dynamically
for i in range(1,15):
    for j in range(1,i+2):
        T[i][j] = T[i][j]+max(T[i-1][j-1], T[i-1][j])

print max(T[14])
