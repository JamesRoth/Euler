"""
data={}
data["factors"] = []
data["num1"] = 600851475143

from math import *

def loopMe(num):
    for i in range(floor(num**0.5),2,-1):
        if num%i==0:
            data["num1"]=data["num1"]/i
            data["factors"].append(i)
            print(data["num1"])
            print(data["factors"])
            loopMe(num)

loopMe(data["num1"])
"""

num = 600851475143
factors=[]

from math import *

end = [3, 7, 9, 1]

def prime(num):
    if int(str(num)[-1]) in end:
        
    else:
        return("none")

for i in range(floor(num**0.5),1,-1):
    if num%i==0 and i!=num:
        num=num/i
        factors.append(i)
        print(num)
        print(factors)
print(num)