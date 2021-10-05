from exercise_sheet2 import exercise_2


def check_none(*args):
    if None in args:
        print("you have not fill in all the fields")
        raise ValueError


def test_exercise_2():
    a, b, c, d = exercise_2()
    check_none(a, b, c, d, e, f)
    assert a is False
    assert b is True
    assert c is False
    assert d is True
