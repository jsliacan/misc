
f = open("data11.txt", "r")
        
grid = [[ int(x) for x in line.split()] for line in f]

maxprod = 0

for i in range(20):
    for j in range(20):
        p1,p2,p3,p4 = 1,1,1,1
        if j < 17:
            for k in range(4): p1 *= grid[i][j+k] # horizontal
        if i < 17:
            for k in range(4): p2 *= grid[i+k][j] # vertical
        if i > 2 and j < 17:
            for k in range(4): p3 *= grid[i-k][j+k] # /
        if i < 17 and j < 17:
            for k in range(4): p4 *= grid[i+k][j+k] # \
        maxprod = max([maxprod, p1, p2, p3, p4])

print maxprod
