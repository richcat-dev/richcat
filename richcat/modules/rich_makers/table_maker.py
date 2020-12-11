from rich.table import Table

from .template import AbstractRichMaker


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
