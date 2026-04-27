list = []


def add_element(adding_value):
    list.append(adding_value)


def user_input():
    user_input = float(input("please add the next element in the list: "))
    return user_input


addvalue = user_input()
add_element(addvalue)

addvalue = user_input()
add_element(adding_value=addvalue)

addvalue = user_input()
add_element(addvalue)
addvalue = user_input()
add_element(addvalue)
print(list)
