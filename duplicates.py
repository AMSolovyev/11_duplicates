import os
from collections import defaultdict
import sys


def get_size_name_file_and_path_dict(path):
    found_size_name_file_and_path_dict = defaultdict(list)
    for root, _, my_files in os.walk(path):
        for my_file in my_files:
            file_path = os.path.join(root, my_file)
            file_size = os.path.getsize(file_path)
            found_size_name_file_and_path_dict['{}_{}'.format(
                my_file, file_size)].append(file_path)
    return found_size_name_file_and_path_dict


def find_duplicates(size_name_file_and_path_dict):
    return [file_path
            for file_path in size_name_file_and_path_dict.values()
            if len(file_path) > 1]


def print_duplicates(duplicates):
    if duplicates is None:
        print('Дубликаты файлов не найдены ')
    else:
        print('Найдены дубликаты')
        delimiter = '=' * 100
        for path in duplicates:
            print(delimiter)
            for path in path:
                print(path)


if __name__ == '__main__':
    work_dir = input('Input the dirname:   ')
    if len(sys.argv) == 1:
        print('Рабочая директория:  {}'.format(work_dir))
    else:
        print('There is not any parametrs on input ')

    size_name_file_and_path_dict = get_size_name_file_and_path_dict(work_dir)
    duplicates = find_duplicates(size_name_file_and_path_dict)
    print_duplicates(duplicates)
