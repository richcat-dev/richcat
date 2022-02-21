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


def is_installed(library_name):
    """
    The function to check if the library is installed

    Parameters
    ----------
    library_name : str
        library name

    Returns
    -------
    : bool
        True if the library is installed
    """
    return os.path.exists(os.popen(f'which {library_name}', 'r').read().split('\n')[0])
