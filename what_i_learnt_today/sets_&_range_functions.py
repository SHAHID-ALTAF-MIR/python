# set
n = set(["shahid", "altaf", "mir"])
print(n)
n = set("shahid")
print(n)

# range function
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dup_list = my_list  # it just copies the reference not the value so if we make the changes in the dup_list the will be reflected in the my_list also
dup_list[0] = 11
print(dup_list)
print(my_list)

# so what we do is that we use the range function
MY_LIST = [1, 2, 3, 4, 5]
DUP_LIST = MY_LIST[:]
# so if we make changes in the DUP_LIST they would not effectg the MY_LIST
DUP_LIST[0] = 7
print(DUP_LIST)
print(MY_LIST)
