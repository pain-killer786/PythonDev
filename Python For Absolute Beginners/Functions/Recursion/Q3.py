# Make a function which calculates a raised to the power b using recursion

 
def power(n,x):
    
    if x==0: #Base Case -> Tells the dunction where to stop
        return 1
    else:
        ans=n*power(n,x-1) #recursive case 
        return ans

a=int(input("Enter a number"))
b=int(input("Enter the power"))
print("The result is", power(a,b))