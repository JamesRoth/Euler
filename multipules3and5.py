#James Roth
#5/7/18
#mulipules3and5.py

total=0
i=3
add=2
while i<1001:
    total+=i
    if add==2:
        i+=add
        add=3
    if add==3:
        i+=add
        add=2
print(total)
