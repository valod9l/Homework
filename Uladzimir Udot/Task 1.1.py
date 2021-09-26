"""Write a Python program to calculate the length
of a string without using the 'len' function."""

text_string = input("Please, enter the text: ")
length_string = 0
for c in text_string:
    length_string += 1
print(f"Length of string: {length_string}")