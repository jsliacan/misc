#!/usr/bin/env python3

"""
Run in Python 3.x as:

   $ python3 bday.py

"""


import datetime

rawbday = input("Enter your birthday (DD/MM/YYYY): ")

bday = [int(x) for x in rawbday.split('/')]
bday = datetime.date(bday[2], bday[1], bday[0])

today = datetime.date.today()

age_d = (today-bday).days
age_y = today.year - bday.year -1


print("\nAge in days:\t", age_d)
print("Age in years:\t", age_y)

timedist = int(input("Enter the milestone in days (integer): "))
celebrate_next = (bday+datetime.timedelta(timedist)).strftime("%A, %-d %B %Y")
print("\nCelebrate", timedist, "days on", celebrate_next)
