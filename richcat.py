from __future__ import unicode_literals
import os
import argparse
from rich.console import Console
from rich.markdown import Markdown

parser = argparse.ArgumentParser(description="RichCat")
parser.add_argument('filepath', type=str, metavar='FilePath', help='file path')
parser.add_argument('-t', '--filetype', type=str, nargs='?', default='auto', metavar='FileType', help='filetype')
args = parser.parse_args()

print(args.filepath)
console = Console()
if args.filetype=='md':
    with open(args.filepath) as f:
        markdown = Markdown(f.read())
    console.print(markdown)

