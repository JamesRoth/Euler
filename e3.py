factors = []
num1 = 600851475143

from math import *

def loopMe(num):
    for i in range(floor(num**0.5),2,-1):
        if num%i==0:
            num1=num/i
            factors.append(i)
            print(num)
            print(factors)
            loopMe(num)

loopMe(num1)
