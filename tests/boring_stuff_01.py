from exercise_sheet2 import *
from random import randint

def test_exercise():
    question = input()
    # exercise 1
    if question == "1a": assert exercise_1a() == 1
    if question == "1b": assert exercise_1b() == 2
    if question == "1c": assert exercise_1c() == 4
    if question == "1d": assert exercise_1d() == 4
    if question == "1e": assert exercise_1e() == 4
    # exercise 2
    if question == "2a": assert exercise_2a() == False
    if question == "2b": assert exercise_2b() == True
    if question == "2c": assert exercise_2c() == False
    if question == "2d": assert exercise_2d() == True
    
if __name__ == "__main__":
    test_exercise()
