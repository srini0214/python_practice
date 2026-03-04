import random
import time
import memory_profiler


names = ['John', 'Jane', 'Jim', 'Jill']
majors = ['Math', 'Engineering', 'Computer Science', 'Art', 'Business']

print(f"Memory (Before): {memory_profiler.memory_usage()}")

#List Comprehension
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

#Generator
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

#Timing the functions
list_time = time.perf_counter()
people_list(1000000)
list_time = time.perf_counter() - list_time
print(f"List time: {list_time} seconds")

generator_time = time.perf_counter()
people_generator(1000000)
generator_time = time.perf_counter() - generator_time
print(f"Generator time: {generator_time} seconds")

print(f"Memory (After): {memory_profiler.memory_usage()}")
