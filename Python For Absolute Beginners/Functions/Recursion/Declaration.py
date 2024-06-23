# A function that calls itself is called recursion.
def factorial(n):
    ans=1
    if n==0: #Base Case -> Tells the dunction where to stop
        return 1
    else:
        ans=n*factorial(n-1) #recursive case 
        return ans

a=int(input("Enter a number"))
print("The result is", factorial(a))
