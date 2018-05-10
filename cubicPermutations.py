#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

cubeMe=0
cubes=[]

def sortInt(num): #sorts an individual list item
    listSort=[]
    for i in range(0, len(str(num))):
        listSort.append(str(num)[i])
    listSort.sort()
    return(listSort)

def checkList(cubes):
    for i in range(6000,len(cubes),-1): #checks sorted list for matches
        if cubes.count(cubes[i]) == 6: #if exactly five (+1 for the original) matches, return cube that matched
            print(cubes[i])
            print(i)
            return(i)
    print(cubes)
    return("none")

while cubeMe<=6000: #main loop
    cubes.append(sortInt(cubeMe**3))
    if cubeMe == 6000:
        ans = checkList(cubes)
        if ans != "none": #if match returned, print match
            print("Ans: ", ans)
        if ans == "none":
            print("Failed")
    cubeMe+=1
