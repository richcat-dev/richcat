from __future__ import unicode_literals
import os
import argparse

from rich.console import Console

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


def make_rich(filepath, filetype):
    """
    The function which make rich text

    Parameters
    ----------
    filepath : str
        filepath
    filetype : str
        filetype

    Returns
    -------
    text : *
        rich text
    """
    if filetype == 'md':
        maker = MarkdownMaker(filepath)
        return maker.make()

    elif filetype == 'csv':
        maker = TableMaker(filepath)
        return maker.make()

    else:
        maker = SyntaxMaker(filepath)
        return maker.make()


def main():
    """ Args """
    parser = argparse.ArgumentParser(description="RichCat")
    parser.add_argument('filepath', type=str, metavar='FilePath', help='file path')
    parser.add_argument('-t', '--filetype', type=str, nargs='?', default='auto', metavar='FileType', help='filetype')
    parser.add_argument('-w', '--width', type=str, nargs='?', default='1.0', metavar='Width', help='width')
    parser.add_argument('-c', '--color_system', type=str, nargs='?', default='256', choices=['standard', '256', 'truecolor', 'windows'], metavar='Width', help='width')
    args = parser.parse_args()

    """ Deciding TextWidth """
    target_width = decide_text_width(args.width)

    """ Infering FileType """
    filepath, filetype = infer_filetype(args.filepath, args.filetype)

    """ General Preparing """
    console = Console(color_system=args.color_system, width=target_width)

    """ Make Rich """
    console.print(make_rich(filepath, filetype))


if __name__ == '__main__':
    main()
