#James Roth
#5/18/19
#sieveOfE.py - the sieve of eratosthenes

from math import sqrt,floor

num = 12345

a = [True]*(n-1) #no idea what - "should be indexed by ints from 2 to n"

for i in range(2, floor(sqrt(num))+1):
