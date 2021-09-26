"""Write a program which makes a pretty print of a part of the multiplication table."""

a = int(input("Please, enter the 'a' number: "))
b = int(input("Please, enter the 'b' number: "))
c = int(input("Please, enter the 'c' number: "))
d = int(input("Please, enter the 'd' number: "))

multi_table = []
for i in range(a - 1, b + 1):
    res_string = []
    for j in range(c - 1, d + 1):
        if i == a - 1 and j == c - 1:
            res_string.append(' '.ljust(3))
        elif i == a - 1:
            res_string.append(str(j).ljust(3))
        elif j == c - 1:
            res_string.append(str(i).ljust(3))
        else:
            res_string.append(str(i * j).ljust(3))
    multi_table.append(res_string)

for c in multi_table:
    print(*c)