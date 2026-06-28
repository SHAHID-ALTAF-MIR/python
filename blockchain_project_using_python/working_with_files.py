#  "w" ---> write only
f = open("shahid.txt", mode="w")
f.write("hello everybody ! ")
f.close()
# python usually calls close() for us but what if we have ongoing code like
# In these types of case we should always call close()
user_input = input("enter your  name !  ")


# "r" ----> read only
f = open("shahid.txt", mode="r")
file_content = f.read()
print(file_content)
f.close()


# "a" ---> append
f = open("shahid.txt", mode="a")
f.write("asalamu alaikum habbibi ! ")
f.close()
