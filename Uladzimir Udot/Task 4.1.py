"""Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa."""

base_string = input("Please, enter the text: ")


def str_replace(base_str):
    res_string = ""
    for c in base_str:
        if c == "\"":
            res_string += "\'"
        elif c == "\'":
            res_string += "\""
        else:
            res_string += c
    return res_string


if __name__ == "__main__":
    print(str_replace(base_string))
    print(str_replace("\'\'\"\"\'\'"))