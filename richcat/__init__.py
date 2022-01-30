from . import richcat as rc
from .richcat import richcat as exec_richcat
from .modules.consts._const import DIC_DEFAULT_VALUES
from .__information__ import __copyright__, __version__, __license__, __author__, __author_email__, __url__


__copyright__ = __copyright__
__version__ = __version__
__license__ = __license__
__author__ = __author__
__author_email__ = __author_email__
__url__ = __url__
rc = rc


def richcat(filepath=None, file_contents=None, **args):
    """
    The richcat function called from Python script

    Parameters
    ----------
    filepath : str
        filepath
    **args : args
        filetype : str
        width : int or float
        color_system : str
        style : str

    Returns
        None
    -------

    """

    if ((filepath is None) and (file_contents is None)):
        file_contents = 'Please input `filepath` or `file_contents`.'
        args['filetype'] = 'md'
    if filepath is not None:
        file_contents = None

    class Args():
        def __init__(self):
            self.filepath = filepath
            self.file_contents = file_contents
            if file_contents is not None:
                self.filetype = args['filetype'] if 'filetype' in args.keys() else 'text'
            else:
                self.filetype = args['filetype'] if 'filetype' in args.keys() else DIC_DEFAULT_VALUES['filetype']
            self.width = args['width'] if 'width' in args.keys() else DIC_DEFAULT_VALUES['width']
            self.color_system = args['color_system'] if 'color_system' in args.keys() else DIC_DEFAULT_VALUES['color_system']
            self.style = args['style'] if 'style' in args.keys() else ''
            self.help = args['help'] if 'help' in args.keys() else False
    args = Args()

    exec_richcat(args)
