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




