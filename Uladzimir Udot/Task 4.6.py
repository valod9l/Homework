"""Implement a function get_shortest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces ( , \n, \t and so on). If there are multiple longest words in the
string with a same length return the word that occures first."""

text_string = input("Please, enter your text: ")


def get_longest_word(text_str):
    return max(text_str.split(), key=lambda x: len(x))


if __name__ == "__main__":
    print(get_longest_word(text_string))
    print(get_longest_word("Python is simple and effective!"))
    print(get_longest_word("Any pythonista like namespaces a lot."))
