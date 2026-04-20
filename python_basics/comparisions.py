print(bool(10 > 20))
print(bool(50 > 32))
print(bool("bag" > "apple"))
print(bool("bag" == "BAG"))
print(ord("b"))


# ternary operator
age = 12
msg = "eligible" if age >= 18 else "ineligibe"
print(msg)


# lodical operators

# and
# or
# not

hi = False
gc = True
ss = False

if (hi or gc) and not ss:
    print("eligible")
else:
    print("ineligible")


# chaining comparisons operator

# age should be bw 18 and 65

age = 21
if 18 <= age < 65:
    print("eligible")
else:
    print("ineligible")
