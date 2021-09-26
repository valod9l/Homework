"""Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers)
and combines them into one dictionary. Dict values should be summarized in case of identical keys"""


def combine_dicts(*args):
    res_dict = {}
    for c in args:
        for key in c:
            if key in res_dict:
                res_dict[key] += c[key]
            else:
                res_dict[key] = c[key]
    return res_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}


if __name__ == "__main__":
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))
