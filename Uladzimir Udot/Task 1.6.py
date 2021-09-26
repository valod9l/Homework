"""Write a Python program to print all unique values of all dictionaries in a list."""

in_lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"II": "S007"}]
unique_values = set()
for c in in_lst:
    for value in c.values():
        if value not in unique_values:
            unique_values.add(value)
print(unique_values)