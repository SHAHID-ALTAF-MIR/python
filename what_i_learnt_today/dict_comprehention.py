
# dict comprehensions

stat = [("age", 21), ("weight", 70), ("height", 180), (("D0B", 2005))]
print(stat)

dict_stat = {key: value for (key, value) in stat}
print(dict_stat)


# enumerate funtion :: if we wrap  a list in the enumerate function it will give us its index of the element and the element itself
