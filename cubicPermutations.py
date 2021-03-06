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
    for i in range(0, len(cubes)-1): #checks sorted list for matches
        if cubes.count(cubes[i]) == 5: #if exactly five matches, return cube that matched
            print(cubes[i])
            return(i)
    print(cubes)
    return("none")
    """
    answer = [0, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9]
    test = [0, 1, 2, 3, 4, 5, 6, 6]
    print("Test:", cubes.count(test))
    print("AnswerTest:", cubes.count(answer))
    """

while cubeMe<=10000: #main loop
    cubes.append(sortInt(cubeMe**3)) #inputs cubes, then sorts them, returns a list of digits
    cubeMe+=1

ans = checkList(cubes)
if ans != "none": #if match returned, print match
    print("Ans: ", ans)
if ans == "none":
    print("Failed")

