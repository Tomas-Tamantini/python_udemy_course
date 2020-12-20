# Exercise 7 - Read file, replace vowels with * and save to new file
import re

from core.utils.file_io_utils import save_text, get_full_content


def replace_vowels(file_name):
    """
    Saves new file with all vowels in input file text replaced by '*'
    :param file_name: Name of input file in folder io_files
    """

    original_text = get_full_content(file_name)
    if original_text is None or len(original_text) == 0:
        return

    new_text = re.sub('[AEIOUaeiou]', '*', original_text)
    save_text(new_text, 'ex_7_out', overwrite=True)
