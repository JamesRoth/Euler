#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

from itertools import permutations


cubeMe=10
done=0

while done==0:
    cube=cubeMe**3
    list1=[]
    for p in permutations(str(cube)):
        list1.append(p)
    done=1
    print(list1)

"""
listTest = ["a", "b", "c", "d"]
num=12345
for p in permutations(str(num)):
    print(p)
"""
