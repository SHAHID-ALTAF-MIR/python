simple_list = [1, 2, 3, 4, 5]
simple_list.extend([1, 2, 3])
print(simple_list)


simple_dict = {"name": "shahid", "class": "10"}
print(simple_dict.items())


simple_tuple = (1, 2, 3, 4, 5)
print(simple_tuple.index(4))

simple_set = {"shahid", "altaf", "mir"}
simple_set.remove("shahid")
simple_set.add("yaseen")
print(simple_set)


# del ---> del is the general function to delete elements from from any data structure except tuples thats because tuples are immutable
del (simple_list[0])
print(simple_list)

del (simple_dict["name"])
print(simple_dict)

# del (simple_set[2])
# print(simple_set)          [to remove elements from the set we use discard as the del function doesnt support deletion in the set as well]


# del (simple_tuple[1])
# print(simple_tuple)


new_list = [True, True, False]
print(any(new_list))  # checks if any elements are true
print(all(new_list))  # checks if all elements are true

# we have to find out if all elements are greater then zero
listt = [1, 2, 3, -5]
# a = [el for el in listt if el > 0]
# print(a)
b = all([el > 0 for el in listt])
print(b)


# unpacking,list comprehension,for loop and indexing  in datastructures

# lists
# unpacking in lists
my_list = [1, 2, 3, 4]
a, b, c, d = my_list
print(a, b, c, d)
# list comprehension in lists
x = [el for el in my_list]
print(x)
# for loop in lists
for el in my_list:
    print(el+1)
# indexing in lists
print(my_list[0])


# sets

# unpacking in sets
my_set = {"shahid", "altaf", "mir"}
a, b, c = my_set
print(a)

# list comprehension in sets
y = [el for el in my_set]
print(y)

# for loop
for el in my_set:
    print(my_set)

# indexing in sets
# print(my_set[1])    (indexing does not work in sets)


# dictionareies

# unpacking in dictionaries
my_dict = {"name": "shahid", "roll_no": 10237}
a, b = my_dict.values()
print(a, b)

# list comprehension in dictionaries
d = [(el, k) for (el, k) in my_dict.items()]
# (included item function so that i could get both keys and values, we can also include value function to inget values only )
print(d)

# for loop in dictionaries
for el in my_dict:
    print(my_dict)

# indexing in dictionaries     (indexing does worki in dictionaries but by the keys)
print(my_dict["name"])

# tuples

# unpacing in tuples
my_tuple = (1, 2, 3, 4)
a, b, c, d = my_tuple
print(a, b, c, d)

# list comprehension in tuples
z = [el for el in my_tuple]
# list comprehension does work in tuple but it gives list as outcome
print(z)

# for loop in tuples
for el in my_tuple:
    print(my_tuple)

# indexing in tuples
print(my_tuple[0])
