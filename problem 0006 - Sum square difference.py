"""
The sum of the squares of the first ten natural numbers is,
                                    1**2+2**2+...+10**2=385

The square of the sum of the first ten natural numbers is,
                                    (1+2+...+10)**2=55**2=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025-385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

print(pow(sum(list(range(1,101))),2)-sum(list(map(lambda n: n**2,list(range(1,101))))))
