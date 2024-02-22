'''
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование
'''
import os
import argparse
import logging
from collections import namedtuple

parser = argparse.ArgumentParser(description="Collect information about files and directories")
parser.add_argument("directory", type=str, help="Path to the directory")

Entry = namedtuple("Entry", ["name", "extension", "is_dir", "parent"])

def collect_directory_info(directory):
    entries = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        is_dir = os.path.isdir(path)
        if is_dir:
            entry = Entry(name=name, extension="", is_dir=True, parent=directory)
        else:
            base_name, extension = os.path.splitext(name)
            entry = Entry(name=base_name, extension=extension, is_dir=False, parent=directory)
        entries.append(entry)
    return entries

if __name__ == "__main__":
    args = parser.parse_args()
    directory = args.directory
    LOG_FORMAT = '%(asctime)s - %(message)s'
    logging.basicConfig(filename='log_task2.log', level=logging.INFO,
                        format=LOG_FORMAT, encoding='utf-8')

    try:
        entries = collect_directory_info(directory)
        with open("directory_info.txt", "w", encoding='utf-8') as file:
            for entry in entries:
                file.write(f"Имя: {entry.name}\n")
                file.write(f"Расширение: {entry.extension}\n")
                file.write(f"Директория: {'Да' if entry.is_dir else 'нет'}\n")
                file.write(f"Родительская директория: {entry.parent}\n")
                file.write("\n")
    except Exception as e:
        logging.error(f"Произошла ошибка: {str(e)}")