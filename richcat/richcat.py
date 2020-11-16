from __future__ import unicode_literals
import os
import argparse
import pandas as pd
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.table import Table

def main():
    """ Args """
    parser = argparse.ArgumentParser(description="RichCat")
    parser.add_argument('filepath', type=str, metavar='FilePath', help='file path')
    parser.add_argument('-t', '--filetype', type=str, nargs='?', default='auto', metavar='FileType', help='filetype')
    parser.add_argument('-w', '--width', type=str, nargs='?', default='1.0', metavar='Width', help='width')
    parser.add_argument('-c', '--color_system', type=str, nargs='?', default='256', choices=['standard', '256', 'truecolor', 'windows'],metavar='Width', help='width')
    args = parser.parse_args()

    """ Deciding TextWidth """
    target_width = float(args.width)
    if target_width<=1.0:
        _, terminal_width = os.popen('stty size', 'r').read().split()
        terminal_width    = float(terminal_width)
        target_width      = int(terminal_width*target_width)
    else:
        target_width = int(target_width)

    """ Infering FileType """
    filetype=args.filetype
    filepath=args.filepath
    if filetype=='auto':
        filetype=filepath.split('.')[-1]

    """ General Preparing """
    console = Console(color_system=args.color_system, width=target_width)
    if filetype=='csv':
        df = pd.read_csv(filepath, header=None)
    else:
        with open(filepath) as f:
            text = f.read()

    """ Make Rich """
    syntax_dict = {
            'py': 'python',
            'rust': 'rust',
            'js': 'javascript',
            'tex': 'tex'
            }
    if filetype in syntax_dict.keys():
        text = Syntax(text, syntax_dict[filetype], line_numbers=True)
    if filetype=='md':
        text = Markdown(text)
    if filetype in ['csv', 'xlsx']:
        text = Table(show_header=True, header_style="bold magenta")
        columns = []
        for col in df:
            text.add_column(str(col))
            columns += [col]
        for index, row in df.iterrows():
            row = [str(row[col]) for col in columns]
            text.add_row(*row)

    console.print(text)

if __name__ == '__main__':
    main()
