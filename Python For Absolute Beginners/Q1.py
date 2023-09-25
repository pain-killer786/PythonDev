# Given a String and a number N, we need to mirror the characters from the N-th position up to the length of the string in alphabetical order. In mirror operation, we change 'a' to'z','b' to'y' and so on. Input: N=3 paradox -> paizwlc

input_string=input("Enter the size of list")
n=int(input("Enter the position"))

#Crearing dictionary for mirror operation
alphabets="abcdefghijklmnopqrstuvwxyz"
reverse_alphabets=alphabets[::-1]
dict1=dict(zip(alphabets,reverse_alphabets))

#finding the part of the string on which we will do mirror operation

prefix=input_string[0:n-1]
suffix=input_string[n-1:]

#finding the mirror string
mirror =""
for i in range(0,len(suffix)):
    mirror=mirror+dict1[suffix[i]]
    
#Creating the final string
res= prefix+mirror
print("The result is: ",res)
