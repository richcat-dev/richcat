import os

from abc import ABC
from abc import abstractmethod

from rich.markdown import Markdown
from rich.table import Table
from rich.syntax import Syntax
from rich.panel import Panel
from rich.console import RenderGroup

from .utils import extract_filename, extract_extension
from ._ext2alias_dic_generator import DIC_LEXER_WC, DIC_LEXER_CONST


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

    def print(self, console, dic_style):
        """
        print rich text

        Parameters
        ----------
        console : rich.console.Console
            console
        dic_style : dict
            style dict
        
        See Also
        --------
        richcat.richcat.interpret_style
        """
        rich_text = self._make_rich_text(self._read_file(), dic_style)
        if dic_style['pager']:
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
    def _make_rich_text(self, file_contents, dic_style):
        """
        rich maker method

        Paremters
        ---------
        file_contents : str
            file contents
        dic_style : dict
            style dict
        
        Returns
        -------
        : str
            rich text

        See Also
        --------
        richcat.rich_maker.AbstractRichMaker.print
        """
        return file_contents


class SyntaxMaker(AbstractRichMaker):
    """ Syntax maker """

    def _read_file(self):
        with open(self.filepath) as f:
            file_contents = f.read()
        return file_contents

    def _make_rich_text(self, file_contents, dic_style):
        return Syntax(file_contents, self.filetype, line_numbers=True)


class MarkdownMaker(AbstractRichMaker):
    """ Markdown maker """

    def _read_file(self):
        with open(self.filepath) as f:
            file_contents = f.read()
        return file_contents

    def _make_rich_text(self, file_contents, dic_style):
        return Markdown(file_contents)


class TableMaker(AbstractRichMaker):
    """ Table maker """

    def _read_file(self):
        lst_table = []
        with open(self.filepath) as f:
            for l in f.read().splitlines():
                lst_table.append(l.split(','))
        return lst_table

    def _make_rich_text(self, file_contents, dic_style):
        # Instance
        text = Table(show_header=True, header_style="bold magenta")
        # Generate table
        columns = []
        if dic_style['header']:
            # Use the 1st line as header

            # Add columns
            for col in file_contents[0]:
                text.add_column(col)
            # Add rows
            for row in file_contents[1:]:
                text.add_row(*row)
        else:
            # Use enumerate number as header
            
            # Add columns
            for col in range(len(file_contents[0])):
                text.add_column(str(col))
                columns += [col]
            # Add rows
            for row in file_contents:
                text.add_row(*row)
        return text
