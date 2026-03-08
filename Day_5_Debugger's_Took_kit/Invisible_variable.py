#Exercise 1: The "Invisible" Variable

#Task: Download a small script that has a logical error (e.g., a loop that skips the last item). 
# Use VS Code Breakpoints to watch the loop index and find the "Off-by-one" error.

def invisible_var():
    a = [1,2,3,4,5]
    for i in a[:-1]:
        print(i)


invisible_var()
