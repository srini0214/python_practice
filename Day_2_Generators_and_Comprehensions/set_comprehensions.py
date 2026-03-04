#Set Comprehensions

duplicate_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_set = {x for x in duplicate_nums}
print(my_set)