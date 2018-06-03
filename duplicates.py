import os
from collections import defaultdict
import sys


def get_size_name_file_and_path_dict(path):
    found_size_name_file_and_path_dict = defaultdict(list)
    for root, _, my_files in os.walk(path):
        for my_file in my_files:
            file_path = os.path.join(root, my_file)
            file_size = os.path.getsize(file_path)
            found_size_name_file_and_path_dict[
                (my_file, file_size)].append(file_path)
    return found_size_name_file_and_path_dict


def get_duplicates(size_name_file_and_path_dict):
    return {file_info: paths for file_info, paths in size_name_file_and_path_dict.items()
            if len(file_info) > 1}


def print_duplicates(duplicates):
    if duplicates is None:
        print('Дубликаты файлов не найдены ')
    else:
        print('Найдены дубликаты')
        delimiter = '=' * 80
        for paths in duplicates:
            print(delimiter)
            for path in paths:
               print(path)


if __name__ == '__main__':
    if len(sys.argv) <2:
        exit('The directory is not specifies')
    work_dir = sys.argv[1]
    if not os.path.isdir(work_dir):
        exit('It is not a directory')
    size_name_file_and_path_dict = get_size_name_file_and_path_dict(work_dir)
    duplicates = get_duplicates(size_name_file_and_path_dict)
    print_duplicates(duplicates)
