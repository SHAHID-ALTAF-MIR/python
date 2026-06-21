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


# "format" method in string
name = "shahid"
age = 21
height = 180
# mathod 1
print("i am {} i am {} old and my height is {}".format(
    name, age, height))
# method 2
print("i am {0} i am {1} old and my height is {2} and my freinds name is also {0}".format(
    name, age, height))
# method 3
print("i am {name} i am {old} old and my height is {tall}".format(
    name=name, old=age, tall=height))

funds = 1509.879
