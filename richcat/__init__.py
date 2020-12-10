from .richcat import infer_filetype, print_rich, is_error_input
from .modules.consts._const import DIC_DEFAULT_VALUES


def richcat(filepath, **args):
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

    class Args():
        def __init__(self):
            self.filepath = filepath
            self.filetype = args['filetype'] if 'filetype' in args.keys() else DIC_DEFAULT_VALUES['filetype']
            self.width = args['width'] if 'width' in args.keys() else DIC_DEFAULT_VALUES['width']
            self.color_system = args['color_system'] if 'color_system' in args.keys() else DIC_DEFAULT_VALUES['color_system']
            self.style = args['style'] if 'style' in args.keys() else ''
    args = Args()

    """ Checking input error """
    if is_error_input(args):
        return

    """ Infering FileType """
    filepath, filetype = infer_filetype(args.filepath, args.filetype)

    """ Print Rich """
    print_rich(filepath, filetype, float(args.width), args.color_system, args.style)
