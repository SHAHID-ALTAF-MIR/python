# Python Program to Find the Factorial of a Number
a = int(input("enter a number!  "))
variable = 1
if a < 0:
    print("the factorial for this number does not exist!  ")
elif a == 0 or a == 1:
    print("the factorial is 1  ")
else:
    for i in range(1, a+1):
        variable = variable*i
    print(variable)
         
