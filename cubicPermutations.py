#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

from itertools import permutations


"""
cubeMe=1
done=0
origPermute=[]

while done==0:
    cube=cubeMe**3
    for num in cube:
        origPermute.append
"""

list1 = ["a", "b", "c", "d"]
num=12345
for p in permutations(str(num)):
    print(p)
