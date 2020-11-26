from __future__ import unicode_literals
import sys
import os
import argparse

from rich.console import Console
from rich.panel import Panel
from rich.console import RenderGroup

from .modules.rich_maker import SyntaxMaker, MarkdownMaker, TableMaker


def decide_text_width(arg_width):
    """
    The function which decide text width.

    Parameters
    ----------
    arg_width : str
        command line argument of width

    Returns
    -------
    : int
        target width
    """
    target_width = float(arg_width)
    if target_width <= 1.0:
        _, terminal_width = os.popen('stty size', 'r').read().split()
        terminal_width = float(terminal_width)
        return int(terminal_width*target_width)
    else:
        return int(target_width)


def infer_filetype(filepath, filetype):
    """
    The function which infer file type

    Parameters
    ----------
    filepath : str
        command line argument of filepath
    filetype : str
        command line argument of filetype

    Returns
    -------
    filepath : str
        filepath
    filetype : str
        filetype
    """
    if filetype == 'auto':
        return filepath, filepath.split('.')[-1]
    else:
        return filepath, filetype


def print_rich(filepath, filetype, console, use_pager):
    """
    The function which make rich text

    Parameters
    ----------
    filepath : str
        filepath
    filetype : str
        filetype
    console : rich.console.Console
        console
    use_pager : bool
            The flag whether use pager
    """
    if filetype == 'md':
        maker = MarkdownMaker(filepath)
        maker.print(console, use_pager)

    elif filetype == 'csv':
        maker = TableMaker(filepath)
        maker.print(console, use_pager)

    else:
        maker = SyntaxMaker(filepath, filetype)
        maker.print(console, use_pager)
            


def main():
    """ Args """
    parser = argparse.ArgumentParser(description="RichCat")
    parser.add_argument('filepath', type=str, metavar='FilePath', help='file path')
    parser.add_argument('-t', '--filetype', type=str, nargs='?', default='auto', metavar='FileType', help='filetype')
    parser.add_argument('-w', '--width', type=str, nargs='?', default='1.0', metavar='Width', help='width')
    parser.add_argument('-c', '--color-system', type=str, nargs='?', default='256', choices=['standard', '256', 'truecolor', 'windows'], metavar='Width', help='width')
    parser.add_argument('--disable-pager', action='store_true', help='flag of disable pager')
    args = parser.parse_args()

    """ Deciding TextWidth """
    target_width = decide_text_width(args.width)

    """ Infering FileType """
    filepath, filetype = infer_filetype(args.filepath, args.filetype)

    """ General Preparing """
    console = Console(color_system=args.color_system, width=target_width)

    """ Print Rich """
    print_rich(filepath, filetype, console, not args.disable_pager)


if __name__ == '__main__':
    main()
