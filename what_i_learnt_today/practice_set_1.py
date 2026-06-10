# Python Program to Print Hello world!
print("hello world")


# Python Program to Add Two Numbers
# method 1
n1 = 1.74
n2 = 3.21
print(n1+n2)

# method 2
a = float(input("eneter a number"))
b = float(input("eneter another number"))
print(a+b)

# method 3
print("the sum of two numbers is  %.2f"
      % (float(input("enetr a number")) + float(input("enter another number"))))


# Python Program to use exponential operator(**)
# method 1
num1 = float(input("eneter a number "))
num2 = float(input("enter another number"))

print(num1**num2)

# method 2
print("%.1f" %
      (float(input("enter a number")) **
       float(input("enter another number"))))


# Python Program to Find the Square Root
# method 1
c = float(input("enter a number "))
print(c**0.5)

# method 2
print("the square root of your number is ", float(input("enetr a number"))**.5)


# Python Program to Calculate the Area of a Triangle
# method 1 (for a right angled triangle)
height = 10
base = 20
print("the area of the triangle is  ", .5*base*height)

# method 2 (for a right angled triangle)
b1 = float(input("enter the base of the triangle "))
h1 = float(input("enter the height of the triangle"))
print("the area of your right angled triangle is ",  .5*b1*h1)

# method 3  (for all  triangles)
s1 = float(input("enter a side of the triangle "))
s2 = float(input("enetr the second side of the triangle"))
s3 = float(input("eneter the third and the last side of the triangle"))
S = (s1+s2+s3)/2  # semi_perimeter
area = (S*(S-s1)*(S-s2)*(S-s3))**0.5
print(f"the area of the triangle is {area} ")
