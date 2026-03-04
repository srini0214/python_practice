#Dictionary Comprehensions

names = ['John', 'Jane', 'Jim', 'Jill']
ages = [20, 21, 22, 23]

name_age_dict = {name: age for name, age in zip(names, ages) if age > 21}
print(name_age_dict)