"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143
d = 3
r = []

while n != 0:

    if n%d == 0:
        r.append(d)
        print("[{}] <---working---> current divisors array {}".format(d,r))
        while n%d == 0:
            n = int(n/d)
        
        d+=1
    
    else:
        d+=1
        print("{} not working tring {} <----> current divisors array {}".format(d-1,d,r))

print(r)