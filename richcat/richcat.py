from __future__ import unicode_literals
import sys
import os
import subprocess
import argparse

from .__information__ import __version__
from .modules.consts._const import LST_COLOR_SYSTEM_CHOISES, DIC_DEFAULT_VALUES
from .modules.consts._ext2alias_dic_generator import DIC_LEXER_WC, DIC_LEXER_CONST
from .modules.exceptions.exception import RichcatFileNotFoundError, RichcatIsDirectoryError, RichcatPermissionError, RichcatBrokenPipeError
from .modules.utils import extract_filename, extract_extension, import_module_with_existence_confirmation
from .modules.help import print_help

from .modules.rich_makers.syntax_maker import SyntaxMaker
from .modules.rich_makers.markdown_maker import MarkdownMaker
from .modules.rich_makers.table_maker import TableMaker


def check_input_error(args):
    """
    The function check input error

    Parameters
    ----------
    args : argparse.Namespace
        command line arguments
    """
    # Is exists
    if args.filepath is None:
        return
    if not os.path.exists(args.filepath):
        raise RichcatFileNotFoundError(args.filepath)
    # Is directory
    if os.path.isdir(args.filepath):
        raise RichcatIsDirectoryError(args.filepath)
    # Is able to access
    if not os.access(args.filepath, os.R_OK):
        raise RichcatPermissionError(args.filepath)


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


def print_rich(filetype, target_width, color_system, style, filepath=None, file_contents=None):
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
    if filetype == 'ipynb':
        if import_module_with_existence_confirmation('jupyter') is not None:
            out, err = subprocess.Popen(f'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to notebook --stdout --log-level WARN {filepath}'.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            out, err = subprocess.Popen(f'jupyter nbconvert --stdin --stdout --to markdown --log-level WARN'.split(' '), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(out)
            file_contents = out.decode('utf-8')
            filepath = None
            filetype = DIC_LEXER_WC['md']
        else:
            filetype = DIC_LEXER_WC['json']

    if filetype == DIC_LEXER_WC['md']:
        maker = MarkdownMaker(target_width, color_system, dic_style, filepath=filepath, file_contents=file_contents)
        maker.print(dic_style['pager'])

    elif filetype == 'csv':
        maker = TableMaker(target_width, color_system, dic_style, filepath=filepath, file_contents=file_contents)
        maker.print(dic_style['pager'])

    else:
        maker = SyntaxMaker(target_width, color_system, dic_style, filepath=filepath, filetype=filetype, file_contents=file_contents)
        maker.print(dic_style['pager'])


def main():
    # Args
    parser = argparse.ArgumentParser(description="RichCat", formatter_class=argparse.RawTextHelpFormatter, add_help=False)
    parser.add_argument('filepath', type=str, metavar='FilePath', nargs='?', default=None, help='file path')
    parser.add_argument('-V', '--version', action='version', version='%%(prog)s %s' % __version__)
    parser.add_argument('-t', '--filetype', type=str, nargs='?', default=DIC_DEFAULT_VALUES['filetype'], metavar='FileType', help='filetype')
    parser.add_argument('-w', '--width', type=float, nargs='?', default=str(DIC_DEFAULT_VALUES['width']), metavar='Width', help='width')
    parser.add_argument('-c', '--color-system', type=str, nargs='?', default=DIC_DEFAULT_VALUES['color_system'], choices=LST_COLOR_SYSTEM_CHOISES, metavar='ColorSystem',
                        help="""color system (default: '256')
    ['standard', '256', 'truecolor', 'windows']""")
    parser.add_argument('--style', type=str, nargs='?', default='', metavar='Style',
                        help="""Style setting
    [[no]header][,[no]pager]""")
    parser.add_argument('-h', '--help', action='store_true')
    args = parser.parse_args()

    if not args.help:
        if args.filepath is None:
            if args.filetype == DIC_DEFAULT_VALUES['filetype']:
                args.filetype = 'text'
            args.file_contents = ''.join(sys.stdin.readlines())
        else:
            args.file_contents = None
    # Execute richcat
    richcat(args)


def richcat(args):
    try:
        # help
        if args.help:
            args.file_contents, args.filetype, args.filepath = print_help()

        # Checking input error
        check_input_error(args)

        # Infering FileType
        filepath, filetype = infer_filetype(args.filepath, args.filetype)

        # Print Rich
        try:
            print_rich(filetype, float(args.width), args.color_system, args.style, filepath=filepath, file_contents=args.file_contents)
        except BrokenPipeError:
            raise RichcatBrokenPipeError()
    except Exception as e:
        if 'print_error' in dir(e):
            e.print_error()
        else:
            raise e
