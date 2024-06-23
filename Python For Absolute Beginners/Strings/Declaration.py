# Syntax
name1='Hello World'
name2="Python is Awesome."
name3='''Strings in Pthon are super fun.''' # used for multi-line strings

# String is a sequence of character written using '' "" or ''' '''.
#Strings are immutable. We can create new string by manupulating the existing string
print (name1,name2,name3)
print(type(name1))
print(type(name2))
print(type(name3))

# Array-like indexing in strings 
text= "Hello, World!"
print(text[0])
print(text[4])
print(text[-1]) #Negative indexing is allowed

#Traversing a string
#Using for loop
for i in text:
    print(i)
    
#using list comprehension
list=[char for char in text]
for i in list:
    print(i)
    
    
# Finding length of a string
print(len(text))

#Finding a character/string in a string
print(text.find('q')) # find()-> returns the index of the first occurence of the character /substring
print(text.find('e'))

# Slicing of a string -> used to get a part of the string
# Syntax
# [start:end]
print(text[1:10])
print(text[:8])
print(text[1:])

#Modifying Strings

# for converting characters to upper case
print(text.upper())

# for converting characters to lower case
print(text.lower())

# For capitalizing the frst character of my string
print(text.capitalize())

# for stripping/removing any trailing whitespaces
str1="      Hello World!"
print(str1.strip())

# replace() -> replace old substring with new substring 'count' no of times
# <Syntax> -> string.replace(old_substring, new_substring, count)

str2= str1.replace('ello', 'worl') # If count is not given, all occurences of old substring are replaced. 
print(str2)

# split()-> used to split the string into a list of substrings
# <Syntax> -> string.split(sep,maxsplit) // By default separator = " "

str3="ria sia wia dia fia mia nia"
list=str3.split()
print(list)

#concatenation
print(text+ str1)

# format() -> String formatting -> used to insert variable values in a string

fruit1="Mango"
fruit2="Apple"
str5= "i have fruits- {f1} and {f2}".format(f1=fruit1,f2=fruit2)
print(str5)