#!/usr/bin/env python3
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

def get_recurring_length(d, base=10):
    remainders = []
    remainder = 1

    #Skip leading zeroes
    while remainder < d:
            remainder *= base

    # Continue finding remainders until we get a repeated remainder
    while True:
        remainder = remainder % d
        if remainder == 0:
            # The decimal ends
            return 0
        if len(remainders) > 0 and remainder in remainders:
            # The remainder is identical to the first, so we would start the
            # recurrance here.
            return len(remainders) - remainders.index(remainder)
        remainders.append(remainder)
        remainder *= base

print(max(range(2,1000), key=lambda d: get_recurring_length(d)))
