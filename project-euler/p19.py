#!/usr/bin/env python

# Problem 19

day = [1,1,1900]
months30 = [4,6,9,11]


def is_leap(year):
    if year%100 == 0:
        return 0 == year%400
    elif year%4 == 0: return True
    else: return False

num_sundays = 0
weekday = 1
while day != [1,1,2001]:
    dd, mm, yyyy = day

    if (weekday == 0) and (dd == 1) and (yyyy>1900): num_sundays += 1

    if (dd < 28) or (dd < 29 and is_leap(yyyy)): # any month
        day = [dd+1, mm,yyyy]            
    elif dd < 30 and not(mm==2): # not february
        day = [dd+1, mm, yyyy]
    elif dd < 31 and not(mm in months30) and not(mm==2): # not 30-month and not february
        day = [dd+1, mm, yyyy]
    else: # if month end
        if mm == 2:
            day = [1,3,yyyy]
        elif mm in months30:
            day = [1,mm+1,yyyy]
        elif mm != 12:
            day = [1,mm+1,yyyy]
        else:
            day = [1,1,yyyy+1]
            
    weekday = (weekday+1)%7
                
print num_sundays
