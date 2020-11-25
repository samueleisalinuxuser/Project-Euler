"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

a,s = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],0

with open("p022_names.txt","r") as file: names = str(file.readlines()[0]).split(",")

for i in names: names[names.index(i)] = i.split("\"")[1].lower()
del i

names.sort()

for i in names:

    tav = 0
    for ii in i: tav+=a.index(ii)+1

    s+=tav*(names.index(i)+1)

del i

print(s)
