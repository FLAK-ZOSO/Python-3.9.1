#!usr/bin/env python3

'''
Python demonstration of the Birthday Paradox.
'''

from random import randint

def Groups(people: int):
    counter = 0
    while True:
        counter += 1
        list_ = []
        for _ in range(people):
            n = randint(1, 366)
            if n in list_:
                return counter
            list_.append(n)

Groups(20) # This should return 2 or 3, since the probability is 48%
Groups(50) # This should return 1, since the probability is 97%
Groups(367) # This MUST return 1, since the probability is 100%