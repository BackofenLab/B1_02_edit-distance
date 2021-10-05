import pytest
from exercise_sheet2 import exercise_1


def check_none(*args):
    if None in args:
        print("you have not fill in all the fields")
        raise ValueError


def test_exercise_1():
    a, b, c, d, e, f = exercise_1()
    check_none(a, b, c, d, e, f)
    assert a is 0
    assert b is 1
    assert c is 2
    assert d is 4
    assert e is 4
    assert f is 4


