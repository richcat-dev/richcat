import os

from abc import ABC
from abc import abstractmethod

from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.syntax import Syntax
from rich.panel import Panel
from rich.console import RenderGroup

from .utils import extract_filename, extract_extension
from ._ext2alias_dic_generator import DIC_LEXER_WC, DIC_LEXER_CONST


class AbstractRichMaker(ABC):
    """ Abstract rich maker class """

    def __init__(self,
                 target_width,
                 color_system,
                 dic_style,
                 filepath=None,
                 file_contents=None,
                 filetype='auto'):
        """
        Constructor

        Parameters
        ----------
        target_width : float
            target_width
        color_system : str
            color system
        dic_style : dict
            style dict
        filepath : str
            filepath (default: None)
        file_contents : str
            file contents (default: None)
        filetype : str
            filetype (default: 'auto')

        See Also
        --------
        richcat.richcat.interpret_style
        """
        # Load file contents
        assert not (filepath is None and file_contents is None)
        if filepath is not None:
            file_contents = self._read_file(filepath)
        # Generate rich text
        self.rich_text = self._make_rich_text(file_contents, filetype, dic_style)

        # Instance console
        self.console = Console(color_system=color_system, width=self._decide_text_width(target_width))

    def print(self, use_pager):
        """
        print rich text

        Parameters
        ----------
        console : rich.console.Console
            console
        use_pager : bool
            flat whether use pager

        See Also
        --------
        richcat.richcat.interpret_style
        """
        if use_pager:
            with self.console.pager(styles=True):
                self.console.print(self.rich_text)
        else:
            self.console.print(self.rich_text)

    def _decide_text_width(self, target_width):
        """
        Deciding text width method

        Parameters
        ----------
        target_width : float
            target_width

        Returns
        -------
        : int
            target width
        """
        if target_width <= 1.0:
            _, terminal_width = os.popen('stty size', 'r').read().split()
            terminal_width = float(terminal_width)
            return int(terminal_width * target_width)
        else:
            return int(target_width)

    @abstractmethod
    def _read_file(self, filepath):
        """
        file reader method

        Parameters
        ----------
        filepath : str
            filepath

        Returns
        -------
        file_contents : str
            file contents
        """
        pass

    @abstractmethod
    def _make_rich_text(self, file_contents, filetype, dic_style):
        """
        rich maker method

        Paremters
        ---------
        file_contents : str
            file contents
        filetype : str
            filetype
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
        pass


class SyntaxMaker(AbstractRichMaker):
    """ Syntax maker """

    def _read_file(self, filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    def _make_rich_text(self, file_contents, filetype, dic_style):
        return Syntax(file_contents, filetype, line_numbers=True)


class MarkdownMaker(AbstractRichMaker):
    """ Markdown maker """

    def _read_file(self, filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    def _make_rich_text(self, file_contents, filetype, dic_style):
        return Markdown(file_contents)


class TableMaker(AbstractRichMaker):
    """ Table maker """

    def _read_file(self, filepath):
        lst_table = []
        with open(filepath) as f:
            for l in f.read().splitlines():
                lst_table.append(l.split(','))
        return lst_table

    def _make_rich_text(self, file_contents, filetype, dic_style):
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
