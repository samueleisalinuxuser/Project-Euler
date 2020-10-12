"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

pn,f1,f2 = [],[],[]

for i in range(999,99,-1):
    for ii in range(100,1000):
        if str(int(i*ii)) == str(int(i*ii))[::-1]:
            pn.append(i*ii)
            f1.append(i)
            f2.append(ii)
            print("[{}*{}] found palindromic number ---> {}".format(i,ii,i*ii))

del i,ii
maxpn = max(pn)
for i in f1:
    for ii in f2:
        if i*ii == maxpn:
            pf1, pf2 = i,ii

print("[{}*{}] max palindromic number product of two 3-digit numbers ---> {}".format(pf1,pf2,maxpn))
