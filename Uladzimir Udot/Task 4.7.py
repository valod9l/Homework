"""Implement a function foo(List[int]) -> List[int] which, given a list of integers, return a new list such that each
element at index i of the new list is the product of all the numbers in the original array except the one at i."""


def foo(int_list):
    res_list = []
    multi_res = 1

    for i in int_list:
        multi_res *= i

    for c in int_list:
        res_list.append(int(multi_res/c))

    return res_list


if __name__ == "__main__":
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))
