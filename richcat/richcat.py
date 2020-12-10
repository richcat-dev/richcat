from __future__ import unicode_literals
import sys
import os
import argparse

from rich.console import Console
from rich.panel import Panel
from rich.console import RenderGroup

from .modules._const import LST_COLOR_SYSTEM_CHOISES, DIC_DEFAULT_VALUES
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

    if filetype == DIC_DEFAULT_VALUES['filetype']:
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


def print_rich(filepath, filetype, target_width, color_system, style):
    """
    The function which make rich text

    Parameters
    ----------
    filepath : str
        filepath
    filetype : str
        filetype
    target_width : float
        target_width
    color_system : str
        color system
    style : str
        command line argument of style
    """
    # Interpret style
    dic_style = interpret_style(style)

    # Print
    if filetype == 'md':
        maker = MarkdownMaker(target_width, color_system, dic_style, filepath=filepath)
        maker.print(dic_style['pager'])

    elif filetype == 'csv':
        maker = TableMaker(target_width, color_system, dic_style, filepath=filepath)
        maker.print(dic_style['pager'])

    else:
        maker = SyntaxMaker(target_width, color_system, dic_style, filepath=filepath, filetype=filetype)
        maker.print(dic_style['pager'])


def main():
    """ Args """
    parser = argparse.ArgumentParser(description="RichCat", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('filepath', type=str, metavar='FilePath', help='file path')
    parser.add_argument('-t', '--filetype', type=str, nargs='?', default=DIC_DEFAULT_VALUES['filetype'], metavar='FileType', help='filetype')
    parser.add_argument('-w', '--width', type=str, nargs='?', default=str(DIC_DEFAULT_VALUES['width']), metavar='Width', help='width')
    parser.add_argument('-c', '--color-system', type=str, nargs='?', default=DIC_DEFAULT_VALUES['color_system'], choices=LST_COLOR_SYSTEM_CHOISES, metavar='ColorSystem',
                        help="""color system (default: '256')
['standard', '256', 'truecolor', 'windows']""")
    parser.add_argument('--style', type=str, nargs='?', default='', metavar='Style',
                        help="""Style setting
[[no]header][,[no]pager]""")
    args = parser.parse_args()

    """ Checking input error """
    if is_error_input(args):
        return

    """ Infering FileType """
    filepath, filetype = infer_filetype(args.filepath, args.filetype)

    """ Print Rich """
    print_rich(filepath, filetype, float(args.width), args.color_system, args.style)


if __name__ == '__main__':
    main()
