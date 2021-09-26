"""Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string by indexes
specified in indexes. Wrong indexes must be ignored."""


def split_by_index(basic_string, indexes):
    flag_index = 0
    result = []
    for ind in indexes:
        result.append(basic_string[flag_index:ind])
        flag_index = ind
    return result


str_test = "pythoniscool,isn'tit?"
ind_list = [6, 8, 12, 13, 18]
if __name__ == "__main__":
    print(split_by_index(str_test, ind_list))
    print(split_by_index("no luck", [42]))
