import math

from rich.panel import Panel
from rich.markdown import Markdown

from ..consts._const import DIC_DEFAULT_VALUES, MD_MERGIN, MD_PADDING
from ..utils import calc_max_line_length
from .template import AbstractRichMaker


class MarkdownMaker(AbstractRichMaker):
    """ Markdown maker """

    def _decide_console_width(self, file_contents, target_width=DIC_DEFAULT_VALUES['width']):
        # Decide target width
        if target_width < DIC_DEFAULT_VALUES['width']:
            # -- Given width rate pattern
            # Get terminal width
            terminal_width = self._get_terminal_width()
            # Calculate target width
            return int(float(terminal_width) * target_width)
        elif math.isclose(target_width, DIC_DEFAULT_VALUES['width']):
            # -- Default pattern
            # Get terminal width
            terminal_width = self._get_terminal_width()
            # Get text width
            text_width = calc_max_line_length(file_contents) + MD_MERGIN
            # Calculate terminal width
            return text_width if text_width < terminal_width else terminal_width
        else:
            # -- Given target width directly pattern
            return int(target_width)

    def _read_file(self, filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    def _make_rich_text(self, file_contents, filetype, dic_style):
        return Panel(Markdown(file_contents), padding=MD_PADDING)
