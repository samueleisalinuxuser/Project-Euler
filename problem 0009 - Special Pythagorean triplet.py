"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
from math import sqrt

for a in range(1,1000):
    for b in range(1000,0,-1):
        c = sqrt(a**2 + b**2)
        if c >= b and b >= a:
            if a**2 + b**2 == int(c)**2 and a+b+int(c) == 1000:
                p = a*b*int(c)
                print(p)
