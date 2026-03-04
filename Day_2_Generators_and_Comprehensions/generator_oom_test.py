import sys
# A: List of squares
a = [x**2 for x in range(1000000)]
# B: Generator of squares
b = (x**2 for x in range(1000000000))

print(f"List Size: {sys.getsizeof(a)} bytes")
print(f"Gen Size: {sys.getsizeof(b)} bytes")