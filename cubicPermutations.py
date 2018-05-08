#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

from itertools import permutations

def consolidate(permute):#the permuated numbers are lists within a list, this just makes them into numbers in a list
    num=0
    for i in range(0,len(permute)):
        for item in permute[i]:
            print(permute[i])
            print(item)
            print(num)
            num=int(str(num)=str(item))
            print(num)
        permute[i]=num
    print(permute)

cubeMe=7
done=0

while done==0:
    cube=cubeMe**3
    list1=[]
    for p in permutations(str(cube)):
        list1.append(p)
    done=1
    consolidate(list1)

"""
listTest = ["a", "b", "c", "d"]
num=12345
for p in permutations(str(num)):
    print(p)
"""
