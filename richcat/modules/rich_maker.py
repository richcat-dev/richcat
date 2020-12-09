import os

from abc import ABC
from abc import abstractmethod

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.table import Table

from .utils import extract_filename, extract_extension, calc_max_line_length
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
        self.console = Console(color_system=color_system, width=self._decide_console_width(file_contents, target_width))

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

    def _get_terminal_width(self):
        """
        Getting terminal width method

        Returns
        -------
        terminal_width : int
            terminal width
        """
        _, terminal_width = os.popen('stty size', 'r').read().split()
        return int(terminal_width)

    def _decide_console_width(self, file_contents, target_width=1.0):
        """
        Deciding text width method

        Parameters
        ----------
        file_contents : str
            file contents (default: 1.0)
        target_width : float
            target_width

        Returns
        -------
        : int
            target width
        """
        # Get terminal width
        terminal_width = self._get_terminal_width()
        # Decide target width
        if target_width < 1.0:
            return int(terminal_width * target_width)
        else:
            return int(terminal_width)

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

    def _decide_console_width(self, file_contents, target_width=1.0):
        # Get terminal width
        terminal_width = self._get_terminal_width()
        # Decide target width
        if target_width < 1.0:
            return int(terminal_width * target_width)
        else:
            # mergin of target width
            MERGIN = 14
            # calc target width
            text_width = calc_max_line_length(file_contents)
            return text_width if text_width + MERGIN < terminal_width else terminal_width

    def _read_file(self, filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    def _make_rich_text(self, file_contents, filetype, dic_style):
        return Panel(Markdown(file_contents), padding=(1, 3, 1, 3))


class TableMaker(AbstractRichMaker):
    """ Table maker """

    def _read_file(self, filepath):
        lst_table = []
        with open(filepath) as f:
            for l in f.read().splitlines():
                lst_table.append(l.split(','))
        return lst_table

    def _make_rich_text(self, file_contents, filetype, dic_style):

        def _make_table_text(text, columns, rows):
            """
            The function make table text

            Parameters
            ----------
            text : rich.table.Table
                table text
            columns : list[str]
                column text list
            rows : list[str]
                row text list

            Returns
            -------
            text : rich.table.Table
                table text
            """
            for col in columns:
                text.add_column(col)
            for row in rows:
                text.add_row(*row)
            return text

        # Instance
        text = Table(show_header=True, header_style="bold magenta")
        # Generate table
        if dic_style['header']:
            # Use the 1st line as header
            text = _make_table_text(text, file_contents[0], file_contents[1:])
        else:
            # Use enumerate number as header
            text = _make_table_text(text, [str(col) for col in range(len(file_contents[0]))], file_contents)
        return text
