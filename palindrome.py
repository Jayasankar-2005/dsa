def palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return palindrome(s[1:-1])
word=input("enter a string::" )
if palindrome(word):
    print("palindrome")
else:
    print("not palindrome")
    