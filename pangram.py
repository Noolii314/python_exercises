#Q/Write a Python function to check whether a string is a pangram or not.
#A/
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b="The quick brown fox jumps over the lAzy dokdlkslg"
s=b.lower()
c=[]
for i in a:
    if i==' ':
        pass
    elif i in s:
        c.append(i)
if len(c)==len(a):
    print('b is panagram')
else:
    print("b isn't pangram")


