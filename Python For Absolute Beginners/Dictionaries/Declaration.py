#dic={"name":20}

# Dictionaries are ordered
# Dictionaries are Changeable
# Dictionaries are unindexed
# Dictionaries doesn't allow duplicates
# Dictionaries can store any datatype

phones={"john": 982528,
        "Rai":46285,
        "Joy": 12345
        }
#printing a dictionary
print(phones)
print(len(phones))#Check length of Dictionary
print(type(phones)) #Check type of Dictionary
print(phones["john"])
print(phones.get("john"))
print(phones.keys())

#Update value in Dict
phones["john"]= 9874
print(phones)

#add elements in a dictionary
phones["Kia"]=2580
print(phones)

#Add key value pair to the dictionary
more_phones ={"Kia":234567}
phones.update(more_phones)
print(phones)

#Delete elements in a dict
phones.pop("john")
print(phones)

phones.popitem() #This will remove the last added item
print(phones)

phones.clear() # This will empty the dict
print(phones)

#printing the elements of a dict
for x,y in phones.items():
    print(x,y)
   
#Nested Dictionary-> 
phones={"Area1":{"x":0,"y":1},"Area2":{"a":5,"b":7}} 
print(phones["Area1"]["y"])
