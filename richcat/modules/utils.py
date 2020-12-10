import os


def extract_filename(path):
    """
    The function extract filename from filepath

    Parameters
    ----------
    path : str
        filepath

    Returns
    -------
    : str
        filename
    """
    return os.path.split(path)[1]


def extract_extension(path):
    """
    The function extract file extension from filepath

    Parameters
    ----------
    path : str
        filepath

    Returns
    -------
    : str
        file extension
    """
    return extract_filename(path).split('.', 1)[-1]


def count_line_length(file_contents):
    """
    The function count line length

    Parameters
    ----------
    file_contents : str
        file contents

    Returns
    -------
    : list[int]
        list of line length
    """
    return [len(line) for line in file_contents.splitlines()]


def calc_max_line_length(file_contents):
    """
    The function calculate max line length

    Parameters
    ----------
    file_contents : str
        file contents

    Returns
    -------
    : int
        max line length
    """
    return max(count_line_length(file_contents))
