def Sum(n1,n2):
    ans=n1+n2
    return ans

a=int(input("Enter a number"))
b=int(input("Enter a number"))
print("The Sum is:",Sum(a,b))

#positional argument
#print("The sum is",Sum(3,2))

#keyword argument(named arguments)
#print("The sum is: ",Sum(n2=6,n1=4))

#Arbitary arguments -> When we don't know how many arguments we have to pass, we use *args

def addAllNumbers(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

output=addAllNumbers(2,4,5,6,9,8,7,4,5,2,1,3,6,5,4,7)
print(output)