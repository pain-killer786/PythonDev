#Items in Tuples are Ordered.
#Lists are Immutable.
#Lists allow Duplicate Values
#Lists can store any datatype
# List can allow mix of different datatypes

colours=("blue","green","yellow") #Creating a Tuple
print(type(colours)) #Check type of Tuple
print(len(colours)) #Check length of Tuple
print(colours[0]) #Positive acessing items in Tuple
print(colours[-1]) #Negative acessing items in Tuple
print(colours[1:3]) #Range acessing items in Tuple

#check if an item is present in Tuple 
if "green" in colours:
    print("Green is a part of Tuple")
    
#Traverse the Tuple
for i in colours:
    print(i)
    
#Concatenate the Tuples 
more_colours=("blue","brown")
colours=colours+more_colours
print(colours)

#unpacking a Tuple
colours1,colours2,colours3,colours4,colours5=colours
print(colours1,colours2,colours3,colours4,colours5)

#Tuples v/s List

#Iterating through a tuple is faster than in a list
#Lists are mutable whereas Tuples are immutable.
#Tuples that contain immutable elements can be used as a key for a dictionary

