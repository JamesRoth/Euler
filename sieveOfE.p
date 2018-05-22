#James Roth
#5/18/19
#sieveOfE.py - the sieve of eratosthenes

"""
from math import sqrt,floor

num = 30

a = [True]*(num-1) #no idea what - "should be indexed by ints from 2 to n"

for i in range(2, floor(sqrt(num))+1):
    if a[i] == True:
        for j in range(i**2, num):
            a[j] = False
print(a)
"""

num = 30
a = []
for i in range(2, num+1):
    a.append(i)

for i in range(0, len(a)-1):
    for j in range(i*2, num+1):
        