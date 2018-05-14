#James Roth
#5/14/18
#largestPalindrome.py - largest palindrome from product of two three digit numbers

def palindrome(num):
    list1 = []
    for item in str(num):
        list1.append(int(item))
    if list1 == list1.reverse:
        print("yes")
    else:
        print("no")
