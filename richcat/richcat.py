from __future__ import unicode_literals
import sys
import os
import argparse

from rich.console import Console
from rich.panel import Panel
from rich.console import RenderGroup

from .modules._ext2alias_dic_generator import DIC_LEXER_WC, DIC_LEXER_CONST
from .modules.utils import extract_filename, extract_extension
from .modules.rich_maker import SyntaxMaker, MarkdownMaker, TableMaker


def is_error_input(args):
    """
    The function check input error

    Parameters
    ----------
    args : argparse.Namespace
        command line arguments

    Returns
    -------
    : bool
        whether input is error
    """
    console = Console()
    # Is exists
    if not os.path.exists(args.filepath):
        console.print(r'[bold red]\[richcat error][/bold red]: "[bold green]' + args.filepath + '[/bold green]": No such file or directory.')
        return True
    # Is directory
    if os.path.isdir(args.filepath):
        console.print(r'[bold red]\[richcat error][/bold red]: "[bold green]' + args.filepath + '[/bold green]" is a directory.')
        return True
    # Is able to access
    if not os.access(args.filepath, os.R_OK):
        console.print(r'[bold red]\[richcat error][/bold red]: "[bold green]' + args.filepath + '[/bold green]": Permission denied.')
        return True
    
    return False


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
        # Extract filename from filepath
        filename = extract_filename(filepath)
        filetype = extract_extension(filepath)
        # Convert extension to alias
        if filename in DIC_LEXER_CONST.keys():
            return filepath, DIC_LEXER_CONST[filename]
        elif filetype in DIC_LEXER_WC.keys():
            return filepath, DIC_LEXER_WC[filetype]
        else:
            return filepath, filetype
    else:
        return filepath, filetype


def interpret_style(style):
    """
    The function interpret style

    Parameters
    ----------
    style : str
        command line argument of style

    Returns
    -------
    dic_style : dict
        style dict
        - structure:
            - 'header': True/False
            - 'pager': True/False
    """
    # Style dict
    dic_style = {
        'header': False,
        'pager': True
    }
    # Split command line args of style
    lst_style = style.split(',')
    # Interpret style
    for key in dic_style.keys():
        if key in lst_style:
            dic_style[key] = True
        if 'no' + key in lst_style:
            dic_style[key] = False
    return dic_style


def print_rich(filepath, filetype, console, style):
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
    style : str
        command line argument of style
    """
    # Interpret style
    dic_style = interpret_style(style)

    # Print
    if filetype == 'md':
        maker = MarkdownMaker(filepath)
        maker.print(console, dic_style)

    elif filetype == 'csv':
        maker = TableMaker(filepath)
        maker.print(console, dic_style)

    else:
        maker = SyntaxMaker(filepath, filetype)
        maker.print(console, dic_style)


def main():
    """ Args """
    parser = argparse.ArgumentParser(description="RichCat", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('filepath', type=str, metavar='FilePath', help='file path')
    parser.add_argument('-t', '--filetype', type=str, nargs='?', default='auto', metavar='FileType', help='filetype')
    parser.add_argument('-w', '--width', type=str, nargs='?', default='1.0', metavar='Width', help='width')
    parser.add_argument('-c', '--color-system', type=str, nargs='?', default='256', choices=['standard', '256', 'truecolor', 'windows'], metavar='Width', help='width')
    parser.add_argument('--style', type=str, nargs='?', default='', metavar='Style',
                        help="""Style setting
[[no]header][,[no]pager]""")
    args = parser.parse_args()

    """ Checking input error """
    if is_error_input(args):
        return

    """ Infering FileType """
    filepath, filetype = infer_filetype(args.filepath, args.filetype)

    """ General Preparing """
    # Deciding TextWidth
    target_width = decide_text_width(args.width)
    # Instancing Console
    console = Console(color_system=args.color_system, width=target_width)

    """ Print Rich """
    print_rich(filepath, filetype, console, args.style)


if __name__ == '__main__':
    main()
