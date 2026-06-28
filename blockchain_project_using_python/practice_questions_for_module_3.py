# create a list of "persons", dictionaries with names,age and list of hobbies for each person, fill in any data you want.
persons = [{"name": "shahid", "age": 21, "hobbies": ["playing", "sleeping", "coding"]},
           {"name": "irfan", "age": 21, "hobbies": [
               "playing", "sleeping", "eating", "studying"]},
           {"name": "saqib", "age": 23, "hobbies": ["playing", "watching movies"]}]
print(persons)

# use a list comprehension to covert this list of persons into a list of names(of the  persons )

names = [person["name"] for person in persons]
print(names)

# use a list comprehention to check wheather all persons are older than 20.

age = all([el["age"] > 20 for el in persons])
print(age)

# copy the persons list such that you can safely edit the name of the first person(without changing the original list)

# copied_persons = persons[:]
copied_persons = [person.copy() for person in persons]
copied_persons[0]["name"] = "yahya"
print(copied_persons)
print(persons)

# unpack the persons of the list into different variables and output the variables.

a, b, c = persons
print("first element of the persons list ", a)
print("second element of the persons list ", b)
print("third element of the persons list ",  c)
