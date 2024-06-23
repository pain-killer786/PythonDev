# Write a program to print sum from 1 to n

def printSum(n):
    
    #base case
    if n==1:
        return 1
    
    #recursive case
    else:
        sum=n + printSum(n-1)
        return sum

x=int(input("Enter a number:"))
print(printSum(x))
