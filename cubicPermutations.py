#James Roth
#5/7/18
#cubicPermuations.py - smallest cube that can be permuted into 5 different cubes

from itertools import permutations


cubeMe=1
done=0

while done==0:
    cube=cubeMe**3
    list1=[permutations(str(num))]
    print(list1)
    done=1

"""
list1 = ["a", "b", "c", "d"]
num=12345
for p in permutations(str(num)):
    print(p)
"""
