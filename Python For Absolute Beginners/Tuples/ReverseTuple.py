input_tuple=(1,2,3,4,5,6,7,8,9)
list=[]
#adding reversed values in a list
for x in reversed(input_tuple):
    list.append(x)
    
output_tuple=tuple(list) #Typecast into tuple
print(output_tuple)
