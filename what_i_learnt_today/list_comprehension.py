simple = [1, 2, 3, 5, 6]

mod_list_0 = [el*2 for el in simple]
print(mod_list_0)

mod_list = [el/2 for el in simple if el % 2 == 0]
print(mod_list)

calc_item = [1, 2, 3, 4]

dup_list = [el for el in simple if el in calc_item]
print(dup_list)
