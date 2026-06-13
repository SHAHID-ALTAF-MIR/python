# Python Program to Check if a Number is Odd or Even
num = int(input("enter any number!  "))
if num % 2 == 0:
    print(f"{num} is an even number! ")
else:
    print(f"{num} is an odd number! ")


# Python Program to Check Leap Year
year = int(input("enter a year!  "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year!  ")
else:
    print("{} is not a leap year".format(year))


# Python Program to Find the Largest Among Three Numbers
a = float(input("enter first number!  "))
b = float(input("enter second number!  "))
c = float(input("enter third number!  "))
if a == b == c:
    print("all the numbers are same!   ")
elif a >= b and a >= c:
    print(f"{a} is the greatest number among the three!  ")
elif b >= a and b >= c:
    print(f"{b} is the greatest number among the three!  ")
else:
    print(f"{c} is the greatest number among the three!  ")


# Python Program to Print all Prime Numbers in an Interval

a = int(input("enter first number!  "))
b = int(input("enter second number!  "))

for i in range(a, b+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
