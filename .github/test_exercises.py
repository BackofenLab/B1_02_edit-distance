from exercise_sheet2 import *

TEMPLATE = "[x] Response: {}"

def test_exercise():
    question = input()
    if question == "1a": print(exercise_1a())
    if question == "1b": print(exercise_1b())
    if question == "1c": print(exercise_1c())
    if question == "1d": print(exercise_1d())
    if question == "1e": print(exercise_1e())
    if question == "2a": print(exercise_2a())
    if question == "2b": print(exercise_2b())
    if question == "2c": print(exercise_2c())
    if question == "2d": print(exercise_2d())
    if question == "3a": print(levenshtein_substitution("ATCACTACTAGCTAGACTG","ACCACTGCTAGGTAGCCTG"))
    if question == "3b": print(levenshtein_deletions("ATCACTACTAGCTAGACTG", "ATCACTACTAGCTAGACTG"))

if __name__ == "__main__":
    test_exercise()
