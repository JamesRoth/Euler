#James Roth
#5/18/19
#sieveOfE.py - the sieve of eratosthenes

num = 30
a = []
for i in range(2, num+1):
    a.append(i)

for i in range(2, len(a)+1):
    for j in range(i*2-2, num-1, i):
        a[j] = 0

print(a)