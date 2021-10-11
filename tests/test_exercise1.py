import pytest
from exercise_sheet2 import exercise_1


def check_none(*args):
    if None in args:
        print("You have not filled in all the fields!")
        raise ValueError


def test_exercise_1():
    a, b, c, d, e, f = exercise_1()
    check_none(a, b, c, d, e, f)
    assert a == 0
    assert b == 1
    assert c == 2
    assert d == 4
    assert e == 4
    assert f == 4


