"""Write a Python program to convert a given tuple of positive integers into an integer."""

pos_int = tuple(map(int, input("Please, enter your numbers through a space: ").split(' ')))
str_res = ''
for value in pos_int:
    str_res += str(value)
int_res = int(str_res)
print(int_res)