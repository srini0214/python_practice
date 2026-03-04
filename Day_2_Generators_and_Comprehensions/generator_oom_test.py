"""
As an architect, you can think of the brackets as memory allocation instructions:

[] (Square Brackets): This is a List Comprehension. It says: "Allocate a block of RAM large enough for 1,000,000 integers right now and fill it."

() (Parentheses): This is a Generator Expression. It says: "Create a small state-machine object that knows how to calculate the next square when I ask for it."

Pro Tip: You might be tempted to call it a "Tuple Comprehension" because of the parentheses, but tuples don't have comprehensions. In Python, () + for logic always results in a Generator.
"""

import sys
# A: List of squares
a = [x**2 for x in range(1000000)]
# B: Generator of squares
b = (x**2 for x in range(1000000000))

print(f"List Size: {sys.getsizeof(a)} bytes")
print(f"Gen Size: {sys.getsizeof(b)} bytes")