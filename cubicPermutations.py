#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

cubeMe=1
cubes=[]
original=[]
numCubes=0

def sortInt(num): #sorts an individual list item
    listSort=[]
    for i in range(0, len(str(num))):
        listSort.append(str(num)[i])
    listSort.sort()
    newNum=0
    for item in listSort:
        newNum = int(str(newNum)+str(item))
    return(newNum)

def checkList(cubes):
    for i in range(0,len(cubes)): #sorts each item in the list
        cubes[i]=sortInt(cubes[i])
    for i in range(0,len(cubes)): #checks sorted list for matches
        if cubes.count(cubes[i]) == 6: #if exactly five (+1 for the original) matches, return cube that matched
            print(cubes[i])
            print(i)
            return(original[i])
    return("none")

while numCubes!=5 and cubeMe<6001: #main loop
    cubes.append(cubeMe**3)
    original.append(cubeMe)
    if cubeMe == 6000:
        ans = checkList(cubes)
        if ans != "none": #if match returned, print match
            print("Ans: ", ans)
    cubeMe+=1
