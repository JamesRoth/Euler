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

palindromes = [0]

for i in range(999,99,-1):
    for i2 in range(i,99,-1):
        num = i*i2
        if num>max(palindromes):
            palindrome(num)

print(max(palindromes))
