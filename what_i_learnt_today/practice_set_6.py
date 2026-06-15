# Python Program to Display the multiplication Table
a = int(input("enter a number!  "))
for i in range(1, 11):
    print(f"{a} x {i} = {a*i}")


# Python Program to Find the Sum of Natural Numbers
num = 0
a = int(input("enter a number!  "))
if a <= 0:
    print("not a natural number")
else:
    for i in range(1, a+1):
        num = num+i
    print(num)

# Python Program to Find Numbers Divisible by Another Number
dividend = int(input("enter a divident !  "))
divisor = int(input("enter a divisor !  "))
if divisor== 0:
    print("not defined")
elif dividend % divisor == 0:
    print(f"{dividend}  is divisible by {divisor}")
else:
    print(f"{dividend} is not divisible by {divisor}")
