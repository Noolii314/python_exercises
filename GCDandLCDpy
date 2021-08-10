#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
x = int(input('x='))
y = int(input('y='))
def GCD(x,y):
    if x<=0 or y<=0:
        print('function is not defined')
    else :
        a = []
        for i in range(1, x * y):
            if x % i == 0 and y % i == 0:
                a.append(i)
        if max(a) == 1:
            print("x and y have no common factor greater than 1")
        else:
            print(f'greatest common divisor betewen {x} and {y} is {max(a)} ')
GCD(x,y)

#Write a Python program to get the least common multiple (LCM) of two positive integers.
x = int(input('x='))
y = int(input('y='))
def LCD(x,y):
    if x<=0 or y<=0:
        print('function is not defined if x or y are smaller or equal zero')
    else :
        a = []
        for i in range(1, (x * y)+1):
            if i % x == 0 and i % y == 0:
                a.append(i)
    print(f'greatest common divisor betewen {x} and {y} is {min(a)} ')
LCD(x,y)





