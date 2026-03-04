nums = [1, 2, 3, 4, 5]

my_nums = [x * 2 for x in nums ]
print(my_nums)

my_even_nums = [x for x in nums if x % 2 == 0]
print(my_even_nums)

# Using lambda function
my_even_list_using_lambda = list(filter(lambda x: x % 2 == 0, nums))
print(my_even_list_using_lambda)

# Nested loops
my_list = [(letter, num) for letter in 'abcd' for num in range(5)]
print(my_list)

#Dictionary Comprehensions