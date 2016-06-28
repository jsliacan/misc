#!/usr/bin/env python

# Problem 67

f = open("data67.txt", "r")
L = []

for line in f: L.append(map(int, line.split()))

for i in range(len(L)-1,0,-1):
    for j in range(len(L[i])-1):
        L[i-1][j] = L[i-1][j]+ max(L[i][j], L[i][j+1])
print L[0][0]
        
