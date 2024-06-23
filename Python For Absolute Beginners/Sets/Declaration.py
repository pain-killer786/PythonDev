#Sets are also containers for storing multiple values in a variable
# Example:- names={}

#Sets are Unordered
#Sets are Immutable
#Sets are Unindexed
#Duplicates are not allowed 
#Any Datatype can be stored 
# Mix of different datatypes

names={"John","Mary","Dave"}
print(names)
print(len(names)) #check length of Set
print(type(names)) #check type of set

#accesing items of set

for i in names:
    print(i)
    
#check if an element exists in a set
if "Sia" in names:
    print("Sia is in the set")
    
#add elements in set
names.add("Ria")
print(names)

#add another sequence in a set
names_list=["ria","kia"]
names.update(names_list)
print(names)

#removing elements from a set
names.remove("John")
print(names)
names.discard("Karen") #Doesn't throw error if the element is not present in the set
print(names)

#joining two sets
s1={'a','b','c'}
s2={'d','f','a'}
s3=s1.union(s2) #Display all the elements of both the sets
print (s3)
s4=s1.intersection(s2) #Display the duplicate elements from both the sets
print(s4)
s5=s1.symmetric_difference_update(s2) # Doesn't display the duplicates from both the sets
print(s5)
