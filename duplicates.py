import os
from collections import defaultdict
import sys


def get_size_name_file_and_path_dict(path):
    found_size_name_file_and_path_dict = defaultdict(list)
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            found_size_name_file_and_path_dict['{}_{}'.format(
                file, file_size)].append(file_path)
    return found_size_name_file_and_path_dict


def find_duplicates(size_name_file_and_path_dict):
    return [file_path
            for file_path in size_name_file_and_path_dict.values()
            if len(file_path) > 1]


def input_dir_name_or_exit():
    if len(sys.argv) == 1:
        print('There is not any parametrs on input ')
        work_dir = input("Input the dirname:     ")
    else:
        work_dir == sys.argv[1]
        if os.path.isdir(work_dir) and os.path.exists(work_dir):
            print('Рабочая дректория:  {}'.format(work_dir))

    if not os.path.isdir(work_dir):
        print('Указанный путь {} не является директорией'.format(work_dir))
        return None
    if not os.path.exists(work_dir):
        print('Пути к папке не существует:  '.format(work_dir))
        return None

    return work_dir


def print_duplicates(duplicates):
    if duplicates is None:
        print('Дубликаты файлов не найдены ')
    else:
        print('Найдены дубликаты')
        for path in duplicates:
            print('=' * 100)
            for path in path:
                print(path)


if __name__ == '__main__':
    dir_name = input_dir_name_or_exit()
    size_name_file_and_path_dict = get_size_name_file_and_path_dict(dir_name)
    duplicates = find_duplicates(size_name_file_and_path_dict)
    print_duplicates(duplicates)
