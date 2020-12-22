def try_parse_int(str_value):
    """
    Parse string into an int
    :param str_value: Input string value
    :return: Tuple with success status (bool) and parsed value
    """
    try:
        value = int(str_value)
    except ValueError:
        return False, 0
    return True, value


def try_parse_float(str_value):
    """
        Parse string into float
        :param str_value: Input string value
        :return: Tuple with success status (bool) and parsed value
        """
    try:
        value = float(str_value)
    except ValueError:
        return False, 0.0
    return True, value
