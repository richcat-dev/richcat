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
