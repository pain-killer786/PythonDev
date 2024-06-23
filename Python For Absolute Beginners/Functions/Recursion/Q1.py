# Write a program to Print numbers from n to 1.
   
def printNumbers(x):
    if x==0:
        return
    
    print (x)
    printNumbers(x-1)
    
n=int(input("Enter a number"))
printNumbers(n)
