from abc import ABC
from abc import abstractmethod

from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.table import Table


class iRichMaker(ABC):
    """ Rich maker interface """
    
    def __init__(self, filepath):
        """
        Constructor
        
        Parameters
        ----------
        filepath : str
            filepath
        """
        self.filepath = filepath

    def make(self):
        """ executor of rich making """
        return self._write(self._read())

    @abstractmethod
    def _read(self):
        """ file reader """
        pass

    @abstractmethod
    def _write(self, file_contents):
        """ rich maker """
        return file_contents


class SyntaxMaker(iRichMaker):
    """ Syntax maker """

    def _read(self):
        return None

    def _write(self, file_contents):
        return Syntax.from_path(self.filepath, line_numbers=True)


class MarkdownMaker(iRichMaker):
    """ Markdown maker """

    def _read(self):
        with open(self.filepath) as f:
            file_contents = f.read()
        return file_contents

    def _write(self, file_contents):
        return Markdown(file_contents)


class TableMaker(iRichMaker):
    """ Table maker """

    def _read(self):
        lst_table = []
        with open(self.filepath) as f:
            for l in f.read().splitlines():
                lst_table.append(l.split(','))
        return lst_table

    def _write(self, file_contents):
        # Instance
        text = Table(show_header=True, header_style="bold magenta")
        # Add columns
        columns = []
        for col in range(len(file_contents[0])):
            text.add_column(str(col))
            columns += [col]
        # Add rows
        for row in file_contents:
            text.add_row(*row)
        return text