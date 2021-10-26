from exercise_sheet2 import *
from random import randint

def test_exercise():
    question = input()
    #exercise 3.a
    if question == "3a":
        correct_subs = ""
        provided_subs = ""
        for _ in range(10):
            seq1, seq2 = deletion_generator()
            correct_subs = levenshtein_substitution_correct(seq1, seq2)
            provided_subs = levenshtein_substitution(seq1, seq2)
            if correct_subs != provided_subs:
                print("[Your solution provided the wrong result on:\n"
                      f"First sequence: {seq1}\n"
                      f"Second sequence: {seq2}\n"
                      f"Your answer is {provided_subs}, the correct answer is {correct_subs}")
                assert correct_subs == provided_subs
    
if __name__ == "__main__":
    test_exercise()
