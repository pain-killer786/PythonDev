#Faulty Calculator

print("Calculator")

print("Enter your 1st Number")

num1 = int(input())

print("Enter your 2nd number")

num2 = int(input())

print("Please Choose your operator +,*,/")

opp = input()

if opp == "+":

    if num1 == 56 and num2 == 9:

        print("Addition of Two number: 77")

    else:

        print("Addition of Two number:",num1,num2,"=",num1+num2)

elif opp == "*":

    if num1 == 43 and num2 == 3:

        print("Multiplication of Two number: 555")

    else:

        print("Multiplication of Two number:",num1,num2,"=",num1*num2)

elif opp == "/":

    if num1 == 56 and num2 == 6:

        print("Multiplication of Two number: 4")

    else:

        print("Division of Two number:",num1,num2,"=",num1/num2)

else:

    print("Your input is Wrong") 