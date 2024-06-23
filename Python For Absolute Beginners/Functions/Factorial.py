def Factorial(n):
    prod=1
    for i in range(1,n+1):
        prod*=i
    return prod

a=int(input("Enter a number"))
print("The Factorial is:",Factorial(a))
