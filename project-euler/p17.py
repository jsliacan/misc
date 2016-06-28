#!/usr/bin/env python

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decades = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
end = "onethousand"

ndigits = sum([len(x) for x in digits])
nteens = sum([len(x) for x in teens])
ndecades = sum([len(x) for x in decades])
nend = len(end)

n_century = ndigits+nteens+ 10*ndecades + 8*ndigits

# (initial hundred) + (each digit is in "digit hundred and": 900) - (9 occassions when it is without and, e.g. "one hundred") + (each "digit hundred and" has n_century with it) + nend
n_millenium = n_century + 100*(ndigits + 9*len("hundred") + 9*len("and"))- 9*len("and") + 9*n_century + nend


print n_millenium
