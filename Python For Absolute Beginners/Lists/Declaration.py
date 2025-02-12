#Lists are Indexes. Like "Apple" is [0].
#Items in Lists are Ordered.
#Lists are Mutable.
#Lists allow Duplicate Values
#Lists can store any datatype
# List can allow mix of different datatypes

fruits=["Apple","Banana","Guava",6,5,4]
print(fruits)
print(type(fruits)) # checks type of list
print(len(fruits)) # checks length of list
#checking if an item is present in the list
if "Banana" in fruits:
    print("Banana is a part of the list")
if "kiwi" not in fruits:
    print("Kiwi is not part of the list")
#checking if an item is not present in the list
print(fruits[3])
print(fruits[-1])
print([fruits[1:3]])

#functions in List
#append() -> adds item to the end of the list. Example:- list=[10,20,30,45]   list.append(50) -> list=[10,20,30,45,50]
#insert() -> adds item to a particular index in the list
#extend() -> used when a list is appended to another list

fruits.append("Kiwi")
print(fruits)
fruits.insert(3,60)
print(fruits)
more_fruits=["Samsung", "Nokia"]
fruits.extend(more_fruits)
print(fruits)

fruits.remove("Samsung") #Removes Specified Items
print(fruits)
fruits.pop(4) #removes item at a given index or else the last item
print (fruits)

fruits[5]=90 # Changing the value of a given index in a list as list are mutable.
print(fruits)



#list Comprehension -> When we want to make a new list from the existing list

new_fruits=[]
for i in fruits:
    if type(i) is int:
        new_fruits.append(i)
print(new_fruits)

new_fruits.sort()
print(new_fruits)

# List Comprehension