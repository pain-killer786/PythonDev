n=int(input("Enter the size of list:"))

list=[]
for i in range(n):
    num=int(input("Enter the elements of the list:"))
    list.append(num)
    
idx1=int(input("Enter index1: "))
idx2=int(input("Enter index2: "))

temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp

print(list)
