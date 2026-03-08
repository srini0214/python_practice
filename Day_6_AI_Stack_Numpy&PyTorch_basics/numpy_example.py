#Exercise 1: The "Speed Test" (NumPy)

#Task: Create a list of 1,000,000 numbers.

#Time how long it takes to square every number using a standard Python for loop.

#Time how long it takes using np.array(my_list)**2.

#Insight: You should see a 50× to 100× speedup.

import time
import numpy as np

numbers = []
#for i in range(1_000_000):
#    numbers.append(i)

#pythonic : list comprehension
numbers = [i for i in range(1_000_000)]

numberSquare = []

t1 = time.perf_counter()

for j in numbers:
    numberSquare.append(j*j)

t2 = time.perf_counter()

print("time:", t2 - t1)

t3 = time.perf_counter()
squaredArray = np.array(numbers)**2

t4 = time.perf_counter()

print("time diff when using numpy", t4-t3)

