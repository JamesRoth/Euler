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
