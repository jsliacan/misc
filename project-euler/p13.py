"""
python makes this problem too easy
"""

f = open("data13.txt", "r")
s = 0
for line in f: s += int(line)
print str(s)[:10]
