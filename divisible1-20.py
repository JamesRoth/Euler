num1=0
for i in range(1,101):
    num1+=i**2

for i in range(1,101):
    num2+=i
num2=num2**2

print(num2-num1)