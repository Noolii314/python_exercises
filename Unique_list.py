#Q/Write a Python function that takes a list and returns a new list with unique elements of the first list
#A/
a=[1,1,2,3,3,3,3,4,5,5,5,77]
b=[]
for i in range(len(a)-1):
     if a[i]!=a[i+1]:
         b.append(a[i])
b.append(a[len(a)-1])
print(b)

#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
a=[2,6,8,5,9]
def allUniqu(a):
    b = []
    for i in a:
        for j in a:
            if i == j:
                b.append(i)
    if len(a) == len(b):
        return True
    else:
        return False
print(allUniqu(a))








