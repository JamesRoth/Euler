#James Roth
#5/14/18
#largestPalindrome.py - largest palindrome from product of two three digit numbers

def palindrome(num):
    list1 = []
    for i in range(0, len(str(num))):
        list1.append(int(str(num)[i]))
    try:
        list1.reverse
        print("yes")
    except:
        print("no")

palindrome(1001)
palindrome(1221)
palindrome(11034)