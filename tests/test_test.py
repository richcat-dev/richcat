import pytest


@pytest.mark.parametrize(
        "x, y", [
            (1, 1),
            ("a", "a"),
            ]
        )

def test_dummy_test(x, y):
    assert x == y
