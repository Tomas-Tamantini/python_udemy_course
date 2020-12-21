from core.utils.parser_utils import try_parse_int
from user_interface.terminal_ui.section13 import exercise_7
from user_interface.terminal_ui.section13 import exercise_10
from user_interface.terminal_ui.section13 import exercise_25
from user_interface.terminal_ui.section16 import exercise_4
from user_interface.terminal_ui.section17 import exercise_17

exercises = {
    13: {7: exercise_7.main_loop,
         10: exercise_10.main_loop,
         25: exercise_25.main_loop},
    16: {4: exercise_4.main_loop},
    17: {17: exercise_17.main_loop}
}


def main_loop():
    available_sections = tuple(exercises.keys())
    section_inp = input(f'Choose a section {available_sections}, or press "q" to quit: ')
    if section_inp.lower() == 'q':
        return
    parse_successful, section = try_parse_int(section_inp)
    if not parse_successful or section not in available_sections:
        print('Invalid section. Try again.')
    else:
        sub_section_loop(section)
    main_loop()


def sub_section_loop(section):
    available_exercises = tuple(exercises[section].keys())
    exercise = None
    if len(available_exercises) == 1:
        exercise = available_exercises[0]
        print(f'Solution to exercise {available_exercises[0]}:')
    else:
        exercise_inp = input(f'Choose an exercise {available_exercises}, or press "q" to return: ')
        if exercise_inp.lower() == 'q':
            return
        parse_successful, tentative_exercise = try_parse_int(exercise_inp)
        if parse_successful and tentative_exercise in available_exercises:
            exercise = tentative_exercise
    if exercise is None:
        print('Invalid exercise. Try again.')
        sub_section_loop(section)
    else:
        exercises[section][exercise]()
