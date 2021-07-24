#Q/Write a Python function that takes a list and returns a new list with unique elements of the first list
#A/
a=[1,1,2,3,3,3,3,4,5,5,5,77]
b=[]
for i in range(len(a)-1):
     if a[i]!=a[i+1]:
         b.append(a[i])
b.append(a[len(a)-1])
print(b)








