import sys

import pytest

sys.path.append('..')
import richcat.richcat as richcat
import richcat.richcat.modules.exceptions.exception as exc

richcat_init = richcat
richcat = richcat.rc
def create_args(filepath):
    class Args():
        def __init__(self, filepath):
            self.filepath = filepath
    return Args(filepath)

@pytest.mark.parametrize(
        "args, error", [
            (create_args("aaa"), exc.RichcatFileNotFoundError),
            (create_args("debug"), exc.RichcatIsDirectoryError),
            (create_args("debug/test.js"), None)
            ]
        )
def test_check_input_error(args, error):
    try:
        richcat.check_input_error(args)
        assert True
    except Exception as e:
        assert e.__class__ == error(args).__class__

