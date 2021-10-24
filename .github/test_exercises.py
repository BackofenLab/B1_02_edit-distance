from exercise_sheet2 import *

TEMPLATE = "[x] Response: {}"

def test_exercise():
    question = input()
    if question == "1a": assert exercise_1a() == 1
    if question == "1b": assert exercise_1b() == 2
    if question == "1c": assert exercise_1c() == 4

if __name__ == "__main__":
    test_exercise()
