my_text = "shahid"  # immutable
my_list = ["s", "h", "a", "h", "i", "d"]  # mutable
# we can for loop both
for el in my_text:
    print(el)
for el in my_list:
    print(el)

my_list[0] = "y"
print(my_list)  # mutable we can assign value to it
# my_text[0] = "y"  ---> we get 'str' object does not support item assignment

# inbuild help function
# help(my_list)
# help(str)
