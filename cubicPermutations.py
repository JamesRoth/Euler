#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

cubeMe=0
cubes=[]

def sortInt(num): #sorts an individual list item
    listSort=[]
    for i in range(0, len(str(num))):
        listSort.append(int(str(num)[i]))
    listSort.sort()
    return(listSort)

def checkList(cubes):
    for i in range(len(cubes)-1,0,-1): #checks sorted list for matches
        if cubes.count(cubes[i]) == 5: #if exactly five matches, return cube that matched
            print(cubes[i])
            print(i)
            return(i)
    print(cubes)
    return("none")

while cubeMe<=6000: #main loop
    cubes.append(sortInt(cubeMe**3)) #inputs cubes, then sorts them, returns a list of digits
    if cubeMe == 6000:
        #ans = checkList(cubes)
        if ans != "none": #if match returned, print match
            print("Ans: ", ans)
        if ans == "none":
            print("Failed")
    cubeMe+=1
print(cubes.count([1,1,3,3]))