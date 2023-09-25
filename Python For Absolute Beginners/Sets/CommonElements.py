ar1=set([1,5,10,20,40,80])
ar2=set([6,7,20,80,100])
ar3=set([3,4,15,20,30,70,80,120])

ar4=ar1.intersection(ar2.intersection(ar3))
print(list(ar4))