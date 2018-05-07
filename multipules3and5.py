#James Roth
#5/7/18
#mulipules3and5.py

total = []

for i in range(3,1000,3):
    total+=i

for i in range(5,1000,5):
    if i%3!=0:
        total+=i

print(total)
