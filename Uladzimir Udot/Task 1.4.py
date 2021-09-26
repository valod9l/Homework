"""Create a program that asks the user for a number and then prints out a list of all
the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number"""

number = int(input("Please, enter your number: "))
lst_divisors = set()
for i in range(1, number // 2 + 1):
    if number % i == 0:
        lst_divisors.add(i)
    lst_divisors.add(number)
print(lst_divisors)