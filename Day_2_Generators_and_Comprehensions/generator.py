#Generators


def my_square_generator(numbers):
    for num in numbers:
        yield num ** 2

for i in my_square_generator([1, 2, 3, 4, 5]):
    print(i)
