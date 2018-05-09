#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

"""
if abs(round(1000**(1/3),0) - (1000**(1/3))) < 0.0000000001:
    print("sucess")

print(1000**(1/3))

from itertools import permutations

def consolidate(permute): #the permuated numbers are lists within a list, this just makes them into numbers in a list
    for i in range(0,len(permute)):
        num=0
        for item in permute[i]:
            num=int(str(num)+str(item))
        permute[i]=num
    return(permute)

cubeMe=5027 #number to be cubed
done=0

while cubeMe==5027:
    fiveCubes=0
    cube=cubeMe**3
    list1=[]
    for p in permutations(str(cube)):
        list1.append(p)
    list1=consolidate(list1)
    for item in list1:
        if abs(round(item**(1/3),0) - (item**(1/3))) < 0.0000000001:
            fiveCubes+=1
    if fiveCubes==5:
        print(cubeMe)
        done=1
    else:
        cubeMe+=1
        
for p in permutations(str(127035954683)):
    print(p)
"""

cubeMe=1
cubes=[]
original=[]
numCubes=0

def sortInt(num): #sorts an individual list item
    listSort=[]
    for i in range(0, len(num)):
        listSort.append(num[i])
    listSort.sort()
    newNum=0
    for item in listSort:
        newNum = int(str(newNum)+str(item))
    return(newNum)

def checkList(cubes):
    for i in range(0,len(cubes)): #sorts each item in the list
        cubes[i]=sortInt(cubes[i])
    for i in range(0,len(cubes)): #checks sorted list for matches
        if cubes.count(cubes[i]) == 5: #if exactly five matches, return cube that matched
            return(orignals[i])
    return("none")

while numCubes!=5 and cubeMe<5080: #main loop
    cubes.append(cubeMe**3)
    original.append(cubeMe)
    ans = checkList(cubes)
    if ans != "none": #if match returned, print match
        print(ans)
    cubeMe+=1
