from abc import ABC
from abc import abstractmethod

from rich.markdown import Markdown
from rich.table import Table
from rich.syntax import Syntax
from rich.panel import Panel
from rich.console import RenderGroup


class AbstractRichMaker(ABC):
    """ Abstract rich maker class """

    def __init__(self, filepath, filetype='auto'):
        """
        Constructor

        Parameters
        ----------
        filepath : str
            filepath
        filetype : str
            filetype (default: 'auto')
        """
        self.filepath = filepath
        self.filetype = filetype

    def print(self, console, use_pager):
        """
        print rich text
        
        Parameters
        ----------
        console : rich.console.Console
            console
        use_pager : bool
            The flag whether use pager
        """
        rich_text = self._make_rich_text(self._read_file())
        if use_pager:
            with console.pager(styles=True):
                console.print(rich_text)
        else:
            console.print(rich_text)


    @abstractmethod
    def _read_file(self):
        """
        file reader method
        """
        pass

    @abstractmethod
    def _make_rich_text(self, file_contents):
        """
        rich maker method
        
        Paremters
        ---------
        file_contents : str
            file contents

        Returns
        -------
        : str
            rich text
        """
        return file_contents


class SyntaxMaker(AbstractRichMaker):
    """ Syntax maker """

    def _read_file(self):
        with open(self.filepath) as f:
            file_contents = f.read()
        return file_contents

    def _make_rich_text(self, file_contents):
        if self.filetype == 'auto':
            return Syntax.from_path(self.filepath, line_numbers=True)
        else:
            return Syntax(file_contents, self.filetype, line_numbers=True)


class MarkdownMaker(AbstractRichMaker):
    """ Markdown maker """

    def _read_file(self):
        with open(self.filepath) as f:
            file_contents = f.read()
        return file_contents

    def _make_rich_text(self, file_contents):
        return Markdown(file_contents)


class TableMaker(AbstractRichMaker):
    """ Table maker """

    def _read_file(self):
        lst_table = []
        with open(self.filepath) as f:
            for l in f.read().splitlines():
                lst_table.append(l.split(','))
        return lst_table

    def _make_rich_text(self, file_contents):
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
