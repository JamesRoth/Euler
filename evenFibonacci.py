#James Roth
#5/7/18
#evenFibonacci.py - sum of even fibonacci numbers under 4 million

num=0
total=0

fib=[1,2]

while num<4000000:
    num=fib[-1]+fib[-2]
    fib.append(num)
    
for item in fib:
    if item%2==0:
        total+=item
