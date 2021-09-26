"""Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements.
 Pairs should be formed as in the example. If there is only one element in the list return None instead."""


def get_pairs(pairs_list):
    if len(pairs_list) == 1:
        return None
    else:
        res_pairs = [(pairs_list[i-1], pairs_list[i]) for i in range(1, len(pairs_list))]
        return res_pairs


if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))
