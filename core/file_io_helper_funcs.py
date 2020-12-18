# A bunch of file I/O helper functions
import os


def file_path(file_name):
    return os.path.join('io_files', file_name)


def file_exists(file_name):
    full_path = file_path(file_name)
    if not os.path.isfile(full_path):
        return False
    return True


def get_full_content(file_name, split_by_lines=False):
    if not file_exists(file_name):
        print(f'Input file {file_name} was not found')
        return

    input_path = file_path(file_name)

    is_text_file = '.txt' in file_name

    read_mode = 'r' if is_text_file else 'rb'

    with open(input_path, mode=read_mode) as file:
        text = file.read() if not split_by_lines else file.readlines()

    if is_text_file:
        return text

    if not split_by_lines:
        return str(text, 'utf-8')

    return list(map(lambda line: str(line, 'utf-8'), text))


def save_text(text, file_name, overwrite=False):
    with open(file_path(file_name), 'w') as file:
        file.write(text)

    print(f"File '{file_name}' saved successfully")
