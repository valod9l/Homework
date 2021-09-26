"""Open file data/unsorted_names.txt in data folder. Sort the names
and write them to a new file called sorted_names.txt."""


with open('../data/unsorted_names.txt', 'r+', encoding='utf-8') as f, \
        open('sorted_names.txt', 'w', encoding='utf-8') as output:
    result_list = [line.strip() for line in f.readlines()]
    result_list.sort()
    for name in result_list:
        print(name, file=output, sep='\n')
    