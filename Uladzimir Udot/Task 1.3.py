"""Write a Python program that accepts a comma separated
sequence of words as input and prints the unique words in sorted form."""

words_list = ['red', 'white', 'black', 'red', 'green', 'black']
unique_words = []
for c in words_list:
    if c not in unique_words:
        unique_words.append(c)
unique_words.sort()
print(unique_words)