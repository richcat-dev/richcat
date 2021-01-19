"""Exception error classes."""

from abc import abstractmethod

from rich.console import Console


class AbstractRichcatError(Exception):

    """Abstract richcat error class"""

    # Class variables
    ERROR_HEAD = r'[bold red]\[richcat error][/bold red]:'
    console = Console()

    def exec_print(self, error_msg):
        """
        Method execute print process

        Parameters
        ----------
        error_msg : str
            error message
        """
        self.console.print(self.ERROR_HEAD, error_msg)

    @abstractmethod
    def print_error(self):
        pass


class RichcatFileNotFoundError(AbstractRichcatError):
    """
    FileNotFoundError class
    Raise : If input failed because the path does not exist.
    """

    def __init__(self, filepath):
        """
        Constructor

        Parameters
        ----------
        filepath : str
            file path
        """
        self.filepath = filepath

    def print_error(self):
        self.exec_print('"[bold green]' + self.filepath + '[/bold green]": No such file or directory.')


class RichcatIsDirectoryError(AbstractRichcatError):
    """
    IsDirectory class
    Raise : If input failed because it is a directory.
    """

    def __init__(self, filepath):
        """
        Constructor

        Parameters
        ----------
        filepath : str
            file path
        """
        self.filepath = filepath

    def print_error(self):
        self.exec_print('"[bold green]' + self.filepath + '[/bold green]" is a directory.')


class RichcatPermissionError(AbstractRichcatError):
    """
    PermissionError class
    Raise : If input failed because of permission denied.
    """

    def __init__(self, filepath):
        """
        Constructor

        Parameters
        ----------
        filepath : str
            file path
        """
        self.filepath = filepath

    def print_error(self):
        self.exec_print('"[bold green]' + self.filepath + '[/bold green]": Permission denied.')


class RichcatTerminalWidthGetError(AbstractRichcatError):
    """
    TerminalWidthGetError class
    Raise : If 'stty' failed.
    """
    def print_error(self):
        self.exec_print('Cloud not get terminal width. Please give terminal width by using "width" option.')

class RichcatBrokenPipeError(AbstractRichcatError):
    """
    RichcatBrokenPipeError class
    Raise : If pipe is broken.
    """
    def print_error(self):
        pass

