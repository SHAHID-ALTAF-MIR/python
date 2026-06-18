# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
import random
decimal = int(input("enter a decimal number !  "))
user_choice = input(
    "choose the number system you want to convert your decimal to!\n 1: binary\n 2: octal\n 3: hexadecimal\n  ")
if user_choice == "1":
    print(bin(decimal))
elif user_choice == "2":
    print(oct(decimal))
elif user_choice == "3":
    print(hex(decimal))
else:
    print(" you choose an invalid option ! ")


#  Program to find the ASCII value of the given character
user_input = input("enter single character ")
print(f"the ascci value of {user_input} is {ord(user_input)}")

#  Python Program to Find the Factors of a Number
num = int(input("enter an integer! "))
for i in range(1, num+1):
    if num % i == 0:
        print(i)


# Python Program to Generate a Random Number
a = int(input("enter the first  number of the interval !"))
b = int(input("enter the second the number of the interval ! "))
print(random.randint(a, b))
