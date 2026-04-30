# usrinp=float(input("eneter a number"))
# usrinp2=float(input("eneter another number "))
def user_input():
    usrinp = float(input("eneter a number"))
    return usrinp


a = user_input()
b = user_input()

c = input("choose an operator")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
else:
    print("not supported")

