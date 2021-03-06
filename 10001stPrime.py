#James Roth
#5/22/18
#10001stPrime.py - finding the 10001st prime number

def sieve(num):
    a = []
    for i in range(2, num+1):
        a.append(i)

    for i in range(2, len(a)+1):
        for j in range(i*2-2, num-1, i):
            a[j] = 0
    return(a)
    
list1 = sieve(110000)

count = 0

for i in range(0, len(list1)):
    if list1[i] != 0:
        count+=1
    if count == 10001:
        print(list1[i])
        break
print(len(list1))