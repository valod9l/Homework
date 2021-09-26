"""Implement a bunch of functions which receive a changeable number of strings and return next parameters:
    characters that appear in all strings
    characters that appear in at least one string
    characters that appear at least in two strings
    characters of alphabet, that were not used in any string
Note: use string.ascii_lowercase for list of alphabet letters"""

import string


def test_1_1(*args):
    result = set(string.ascii_lowercase)
    for arg in args[0]:
        result.intersection_update(set(arg))
    return result


def test_1_2(*args):
    result = set()
    for arg in args[0]:
        result.update(set(arg))
    return result


def test_1_3(*args):
    result = set()
    for c in string.ascii_lowercase:
        count = 0
        for arg in args[0]:
            if c in arg:
                count += 1
        if count >= 2:
            result.add(c)
    return result


def test_1_4(*args):
    result = set(string.ascii_lowercase)
    for arg in args[0]:
        result.difference_update(set(arg))
    return result


test_strings = ["hello", "world", "python", ]

if __name__ == "__main__":
    print(test_1_1(test_strings))
    print(test_1_2(test_strings))
    print(test_1_3(test_strings))
    print(test_1_4(test_strings))
