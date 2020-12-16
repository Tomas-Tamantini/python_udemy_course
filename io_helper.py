# A bunch of I/O helper functions
import os


def file_path(file_name, section):
    return os.path.join(f'section{section}', 'io_files', file_name)


def file_exists(file_name, section):
    full_path = file_path(file_name, section)
    if not os.path.isfile(full_path):
        return False
    return True


def save_text(text, file_name, section):
    full_path = os.path.join(f'section{section}', 'io_files', file_name)
    with open(full_path, 'w') as file:
        file.write(text)

    print(f"File '{file_name}' saved successfully")
