"""Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a example."""


def most_common_words(filepath, number_of_words=3):
    result = []
    with open(filepath, 'r+', encoding='utf-8') as file:
        res_dict = {}
        words_list = file.read().lower().replace('.', '').replace(',', '').split()
        for word in words_list:
            if word in res_dict:
                res_dict[word] += 1
            else:
                res_dict[word] = 1

        res_dict = sorted(res_dict.items(), key=lambda x: x[1], reverse=True)

        for word in res_dict[:number_of_words]:
            result.append(word[0])

    return result


if __name__ == "__main__":
    print(most_common_words('../data/lorem_ipsum.txt'))
