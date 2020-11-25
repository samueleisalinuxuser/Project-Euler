"""
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
"""

ns = list()

for a in range(1,101):
    for b in range(1,101):
        r = 0
        for i in str(a**b): r+=int(i)
        ns.append(r)

n = max(ns)
print(n)
