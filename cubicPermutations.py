#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

"""
if abs(round(1000**(1/3),0) - (1000**(1/3))) < 0.0000000001:
    print("sucess")

print(1000**(1/3))
"""

from itertools import permutations

def consolidate(permute): #the permuated numbers are lists within a list, this just makes them into numbers in a list
    for i in range(0,len(permute)):
        num=0
        for item in permute[i]:
            num=int(str(num)+str(item))
        permute[i]=num
    return(permute)

cubeMe=1 #number to be cubed
done=0

while done==0:
    fiveCubes=0
    cube=cubeMe**3
    list1=[]
    for p in permutations(str(cube)):
        list1.append(p)
    list1=consolidate(list1)
    for item in list1:
        if abs(round(cube**(1/3),0) - (cube**(1/3))) < 0.0000000001:
            fiveCubes+=1
    if fiveCubes==5 or cubeMe==100:
        print(cubeMe)
        done=1
    else:
        cubeMe+=1
