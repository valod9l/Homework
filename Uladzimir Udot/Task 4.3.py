"""Implement a function which works the same as str.split method (without using str.split itself, ofcourse)."""


def func_split(text, sep=' '):
    result = []
    start = 0
    for i, char in enumerate(text):
        if char == sep:
            list_el = text[start:i]
            if list_el != "":
                result.append(list_el)
            start = i + 1
    last_el = text[start:]
    if last_el != "":
        result.append(last_el)
    return result


text_str = "Implement    a  function   which          works    the  same as str.split                 method."


if __name__ == "__main__":
    print(func_split(text_str))