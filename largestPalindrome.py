#James Roth
#5/14/18
#largestPalindrome.py - largest palindrome from product of two three digit numbers

def palindrome(num):
    list1 = []
    for i in range(0, len(str(num))):
        list1.append(int(str(num)[i]))
    list2 = list1[:]
    list2.reverse()
    if list1 == list2:
        palindromes.append(num)

palindromes = []

"""
for i in range(999,99,-1):
    for i2 in range(999,99,-1):
        palindrome(i*i2)


for i in range(100*100, 999*999):
    palindrome(i)
print(palindromes)
"""