"""File data/students.csv stores information about students in CSV format. This file contains the student’s names,
age and average mark.
    1. Implement a function which receives file path and returns names of top performer students.
    2. Implement a function which receives the file path with students info and writes CSV student
    information to the new file in descending order of age."""


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path) as file:
        result_1 = []
        title = file.readline()
        student_dict = {}
        stud_val = file.read().strip().split('\n')
        for value in stud_val:
            res = value.split(',')
            student_dict[res[0]] = float(res[2])

        res_dict = sorted(student_dict.items(), key=lambda x: x[1], reverse=True)

        for student in res_dict[:number_of_top_students]:
            result_1.append(student[0])

        return result_1


def sorted_students_by_age(file_path):
    with open(file_path) as file, open('sorted_students.csv', 'w', encoding='utf-8') as output:
        title = file.readline()
        result_2 = []
        stud_val = file.read().strip().split('\n')
        for value in stud_val:
            result_2.append(value.split(','))

        result_2 = sorted(result_2, key=lambda x: x[1], reverse=True)
        result_2.insert(0, title.strip().split(','))

        for student in result_2:
            print(', '.join(student), file=output, sep='\n')


if __name__ == "__main__":
    print(get_top_performers('../data/students.csv'))
    sorted_students_by_age('../data/students.csv')
