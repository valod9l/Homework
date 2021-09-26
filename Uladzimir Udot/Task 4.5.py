"""Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits."""


def get_digits(numb):
    res_tuple = tuple((int(num) for num in str(numb)))
    return res_tuple


number = int(input("Please, enter the number: "))
if __name__ == "__main__":
    print(get_digits(475874875))
    print(get_digits(number))

