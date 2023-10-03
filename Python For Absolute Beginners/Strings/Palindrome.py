# Write a Python Function that checks if the given string is a palindrome or not
    
def PalindromeString(str):
    clean_str= (str.replace(" ","")).lower()
    reverse_str=clean_str[::-1]
    return clean_str == reverse_str

str=input("Enter a string")
if PalindromeString(str):
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")