#James Roth
#5/14/18
#largestPalindrome.py - largest palindrome from product of two three digit numbers

def palindrome(num):
    list1 = []
    for i in range(0, len(str(num))):
        list1.append(int(str(num)[i]))
    list2 = list1.reverse
    print(list1)
    print(list2)
    if list1 == list2:
        print("yes")
    else:
        print("no")

palindrome(1001)
palindrome(1221)