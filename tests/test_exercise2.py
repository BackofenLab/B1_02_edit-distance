from sheet_2 import exercise_2


def test_exercise_2():
    a, b, c, d = exercise_2()

    assert a is False
    assert b is True
    assert c is False
    assert d is True
