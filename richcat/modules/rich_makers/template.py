import os

from abc import ABC
from abc import abstractmethod

from rich.console import Console

from ..consts._const import DIC_DEFAULT_VALUES
from ..exceptions.exception import RichcatTerminalWidthGetError


class AbstractRichMaker(ABC):
    """ Abstract rich maker class """

    def __init__(self,
                 target_width,
                 color_system,
                 dic_style,
                 filepath=None,
                 file_contents=None,
                 filetype=DIC_DEFAULT_VALUES['filetype']):
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
        try:
            terminal_width = int(os.popen('tput cols', 'r').read())
            return terminal_width
        except ValueError:
            raise RichcatTerminalWidthGetError()

    def _decide_console_width(self, file_contents, target_width=DIC_DEFAULT_VALUES['width']):
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
        if target_width <= DIC_DEFAULT_VALUES['width']:
            return int(float(terminal_width) * target_width)
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
