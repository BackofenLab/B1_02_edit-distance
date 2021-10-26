from exercise_sheet2 import *
from random import randint

def test_exercise():
    question = input()
    #exercise 3.b

    if question == "3b":
        correct_subs = ""
        provided_subs = ""
        for _ in range(5):
            seq1, seq2 = deletion_generator()
            correct_dels = levenshtein_deletions_correct(seq1, seq2)
            provided_dels = levenshtein_deletions(seq1, seq2)
            if correct_dels != provided_dels:
                print("Your solution provided the wrong result on:\n"
                    f"First sequence {seq1}\n"
                    f"Second sequence {seq2}\n"
                    f"Your answer is {provided_dels}, the correct answer is {correct_dels}")
                assert correct_dels == provided_dels

        for _ in range(5):
            seq1, seq2 = deletion_generator()
            correct_dels = levenshtein_deletions_correct(seq2, seq1)
            provided_dels = levenshtein_deletions(seq2, seq1)
            if correct_dels != provided_dels:
                print("Your solution provided the wrong result on:\n"
                    f"First sequence {seq1}\n"
                    f"Second sequence {seq2}\n"
                    f"Your answer is {provided_dels}, the correct answer is {correct_dels}")
                assert correct_dels == provided_dels

        for _ in range(5):
            seq1, seq2 = substitution_generator()
            correct_dels = levenshtein_deletions_correct(seq2, seq1)
            provided_dels = levenshtein_deletions(seq2, seq1)
            if correct_dels != provided_dels:
                print("Your solution provided the wrong result on:\n"
                    f"First sequence {seq1}\n"
                    f"Second sequence {seq2}\n"
                    f"Your answer is {provided_dels}, the correct answer is {correct_dels}")
                assert correct_dels == provided_dels

# helper functions

def substitution_generator():
    first_seq = "".join(["AGCT"[randint(0, 3)] for _ in range(randint(7, 10))])
    second_seq = list(first_seq)
    for i in range(randint(1, 5)):
        second_seq[randint(0, len(second_seq)-1)] = "AGCT"[randint(0, 3)]
    second_seq = "".join(second_seq)
    return first_seq, second_seq


def deletion_generator():
    first_seq = "".join(["AGCT"[randint(0, 3)] for _ in range(randint(7, 10))])
    second_seq = list(first_seq)
    for i in range(randint(1, 5)):
        second_seq[randint(0, len(second_seq)-1)] = ""
    second_seq = "".join(second_seq)
    return first_seq, second_seq


def levenshtein_substitution_correct(seq1, seq2):
    return sum([1 for a, b in zip(seq1, seq2) if a != b])


def levenshtein_deletions_correct(seq1, seq2):
    seq1, seq2 = sorted([seq1, seq2], reverse=True)

    max_allowed_deletions = len(seq1) - len(seq2)

    current_deletions = []
    num_deletions = 0

    index_first = 0
    index_second = 0

    while num_deletions <= max_allowed_deletions:
        if index_first == len(seq1):
            break
        char_first = seq1[index_first]
        char_second = seq2[index_second]

        if char_first == char_second:
            index_first += 1
            index_second += 1

        else:
            current_deletions.append(index_first)
            num_deletions += 1
            index_first += 1

    else:
        return None

    return num_deletions


    
if __name__ == "__main__":
    test_exercise()
