# Python Program to Solve Quadratic Equation
import cmath
a = float(input("enter first constant of the equation:  "))
b = float(input("enter second constant of the equation:  "))
c = float(input("enter third constant of the equation:  "))

d = (b**2)-(4*a*c)
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)
print(f"first root the quadratic equation is {root1}")
print(f"second root of the quadrative equation is {root2}")


# Python Program to Swap Two Variables
# method 1 (without users input)
a = 10
b = 20
a, b = b, a
print(a, b)
# method 2 (without users input)
# using third variable
a = 20
b = 32
c = a
a = b
b = c
print(a, b)

# method 3 (with users input)
a = float(input("enetr a number:  "))
b = float(input("enter another number:  "))
a, b = b, a
print(f"the variables after swapping are as {a, b}")


# Python Program to Check if a Number is Positive, Negative or 0
# method 1
a = float(input("enetr a number:  "))
if a > 0:
    print(f"this number is a positive number! --> {a}  ")
elif a == 0:
    print(f"this number is zero! --> {a}")
else:
    print(f"the number you entered is a negative number1--> {a}")

# method 2
a = float(input("enter a number!  "))
if a >= 0:
    if a == 0:
        print("number is zero")
    else:
        print("positive number")
else:
    print("negative number")
