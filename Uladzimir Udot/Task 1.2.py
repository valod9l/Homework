"""Write a Python program to count the number
of characters (character frequency) in a string
(ignore case of letter)."""

text_string = input("Please, enter the text: ")
count_char = dict()
for c in text_string.lower():
    if c in count_char:
        count_char[c] += 1
    else:
        count_char[c] = 1
print(count_char)
