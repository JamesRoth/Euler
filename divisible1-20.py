#James Roth
#5/17/18
#divisible1-20.py - smallest number that is divisible by 1-20 evenly

num = 380

factors = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

while True:
    check = 0
    for item in factors:
        if num%item == 0:
            check+=1
    if check == 18:
        print(num)
        break
    num+=2