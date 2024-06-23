# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.
# <Syntax> -> lambda arguments : expression

x=lambda a:a+10
print(x(5))

a=int(input("Enter a number"))
b=int(input("Enter a number"))
x=lambda a, b : (a * b) #-> return part
print(x(a, b))

def myfunc(n):
    return lambda a:a*n

myDoubler=myfunc(2)
myTripler=myfunc(3)

print(myDoubler(11))
print(myTripler(11))
