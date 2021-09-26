"""Write a Python program to sort a dictionary by key."""

some_dict = {'c': 1, 'b': 2, 'w': 5, 'g': 3, 'v': 4}
#sorted(some_dict.keys(), key=lambda x: x)
print(sorted(some_dict.keys(), key=lambda x: x))