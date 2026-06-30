# "w" ---> write only
"""
f = open("shahid.txt", mode="w")
f.write("hello everybody ! ")
f.close()
"""

# python usually calls close() for us but what if we have ongoing code like
# In these types of case we should always call close()
"""
user_input = input("enter your  name !  ")
"""


# "r" ----> read only
"""
f = open("shahid.txt", mode="r")
file_content = f.read()
print(file_content)
f.close()
"""

# "a" ---> append
"""
f = open("shahid.txt", mode="a")
f.write("asalamu alaikum habbibi ! ")
f.close()
"""

# appending the multiline text using \n ---> newline (keyword)
"""
f = open("shahid.txt", mode="a")
f.write("\nasalamu alaikum habbibi !\nhow are you\nwhat is going on\ndid you completed that course")
f.close()
"""

# reading multiline text
"""
f=open("shahid.txt",mode="r")
file_content = f.read()
print(file_content)
"""

# reading single line text
"""
f = open("shahid.txt", mode="r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())  ## By this "print(f.readline())"  will it print each line present in the file after that it will print an empty line
"""
# we can also do this by using a while loop.
"""
f = open("shahid.txt", mode="r")
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()
"""

# reading  multiple lines of text
"""
f=open("shahid.txt",mode="r")
file_content = f.readlines()
print(file_content)
"""

# we operate on the text line by line by using for loop #
"""
for line in file_content:
    print(line[:-1])  # By using -1 in the range selector we will avoid printing '\n' which is treated as a single character
"""


# letting python handle the closing by using "with:" keyword


with open("shahid.txt", mode="w") as f:
    f.write("testing the with keyword ......")
user_input = input("testing")
print("done!")
