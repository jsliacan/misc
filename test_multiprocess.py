
from multiprocessing import Process

from sage.combinat.permutation import Permutations
from sage.doctest.util import Timer

def f(lst):

    for i in range(10):
        for s in lst:
            s.sort()


l = Permutations(10)

timer = Timer().start()
f(l)
print timer.stop()

timer = Timer().start()

print timer.stop()
