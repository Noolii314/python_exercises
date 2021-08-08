#Write a Python program to calculate a dog's age in dog's years
md=float(input('mosha e qenit='))
if md<=2:
    mdn=md*10.5
    print('mosha e qenit sipas viteve te njeriut eshte ',mdn)
elif md>2:
    mdn=((md-2)*4)+21
    print('mosha e qenit sipas viteve te njeriut eshte ',mdn)
# Write a Python program to check whether an alphabet is a vowel or consonant
bashke= [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n','p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
zanore=['a','e','i','o','u','y']
a=input('shkronja e deshiruaar:')
if a in bashke:
    print(f'{a} eshte bashke')
elif a in zanore:
    print(a,'eshte zanore')
#Write a Python program to check a triangle is equilateral, isosceles or scalene
x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
if x==y==z:
    print('trekendesh barabrinjesh')
elif x==y or y==z or x==z:
    print('trekendesh barakrahesh')
else:
    print('treken)

#Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#I
date = (11,12,2014)
print("%i/%i/%i"%date)
#II
print(f"{date[0]}/{date[1]}/{date[2]}")
