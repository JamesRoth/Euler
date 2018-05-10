factors = []
num1 = 600851475143

loopMe(num):
    for i in range(floor(num),1,-1):
        if num%i==0:
            num1=num/i
            loopMe(num)
