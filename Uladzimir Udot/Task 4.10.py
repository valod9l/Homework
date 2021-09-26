"""Implement a function that takes a number as an argument and returns a dictionary, where the key is a number
and the value is the square of that number."""


number = int(input("Please, enter your number: "))


def generate_squares(numb):
    res_dict = {i: i ** 2 for i in range(1, numb + 1)}
    return res_dict


if __name__ == "__main__":
    print(generate_squares(5))
    print(generate_squares(number))

