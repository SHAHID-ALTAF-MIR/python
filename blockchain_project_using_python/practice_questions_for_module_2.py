# 1. create a list of names and use a for loop output the length of each name

names = ["shahid", "altaf", "mir", "gulshana", "tawseef",
         "arooja", "bilqueesa", "yahya", "Nazima", "neelofer"]
for name in names:
    print(name)
    print(len(name))


# 2. add a if check inside the loop to only output names longer than 5 characters
print("_"*50)
for name in names:
    if len(name) > 5:  # checking for the names whose length is greater then 5 characters
        print(name)


# 3. add another if check to see wheather a name includes a "n" or "N" character

print("_"*50)
for name in names:
    if "n" in name or "N" in name:
        print(name)


# 4. add a if chech to check wheather a name starts with "n" or "N"

print("_"*50)
for name in names:
    if name[0] == "n" or name[0] == "N":  # checking for n or N as first letter in the name
        print(name)


# 5. use a while loop to empty the list of names (via pop())
print("_"*50)
while len(names) >= 1:
    print(names.pop())
print(names)
