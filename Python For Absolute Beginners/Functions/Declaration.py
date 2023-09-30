# Functions are blocks of reusable code that performs a specific task
# input --> function --> output

#Types of Function:- 1. Built-in   2.User defined
# <Syntax> -> def function_name(parameters):
#      #statement
#      return expression

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

# **kwargs-> key value pair arguments like used in dictionary
def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
        
studentInfo(name="Krishnendu",age=21,city="Kol")

#Nested Function -> Function inside function
def outer_function():
    x=1
    
    def inner_function():
        y=2
        result=x+y
        return result
    
    return inner_function()
output=outer_function()
print(output)
