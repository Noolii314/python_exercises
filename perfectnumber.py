#Write a Python function that takes a number as a parameter and check the number is prime or not
x = int(input('x='))
def perfectnumber(x):
    l=0
    for i in range(1, x):
        if x % i == 0:
            l += i
    if l == x:
        print(f'{x} is a perfect number')
    else:
        print(f"{x} isn't a perfect number")
perfectnumber(x)


