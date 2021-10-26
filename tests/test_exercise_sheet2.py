from exercise_sheet2 import *
from random import randint
import pytest


def test_exercise1_a():
    assert exercise_1a() == 1


def test_exercise_1b():
    assert exercise_1b() == 2


def test_exercise_1c():
    assert exercise_1c() == 4


def test_exercise_1d():
    assert exercise_1d() == 4


def test_exercise_1e():
    assert exercise_1e() == 4


def test_exercise_2a():
    assert exercise_2a() is False


def test_exercise_2b():
    assert exercise_2b() is True


def test_exercise_2c():
    assert exercise_2c() is False


def test_exercise_2d():
    assert exercise_2d() is True


def deletion_generator():
    first_seq = "".join(["AGCT"[randint(0, 3)] for _ in range(randint(7, 10))])
    second_seq = list(first_seq)
    for i in range(randint(1, 5)):
        second_seq[randint(0, len(second_seq)-1)] = ""
    second_seq = "".join(second_seq)
    return first_seq, second_seq


def substitution_generator():
    first_seq = "".join(["AGCT"[randint(0, 3)] for _ in range(randint(7, 10))])
    second_seq = list(first_seq)
    for i in range(randint(1, 5)):
        second_seq[randint(0, len(second_seq)-1)] = "AGCT"[randint(0, 3)]
    second_seq = "".join(second_seq)
    return first_seq, second_seq


@pytest.mark.parametrize(
    "seq1,seq2",
    [deletion_generator() for x in range(10)]
)
def test_exercise_3a(seq1, seq2):
    correct_subs = levenshtein_substitution_correct(seq1, seq2)
    provided_subs = levenshtein_substitution(seq1, seq2)
    if correct_subs != provided_subs:
        print("[Your solution provided the wrong result on:\n"
              f"First sequence: {seq1}\n"
              f"Second sequence: {seq2}\n"
              f"Your answer is {provided_subs}, the correct answer is {correct_subs}")
        assert correct_subs == provided_subs


@pytest.mark.parametrize(
    "seq1,seq2",
    [deletion_generator() for _ in range(10)] +
    [substitution_generator() for _ in range(10)]
)
def test_exercise_3b(seq1, seq2):
    correct_dels = levenshtein_deletions_correct(seq1, seq2)
    provided_dels = levenshtein_deletions(seq1, seq2)
    if correct_dels != provided_dels:
        print("Your solution provided the wrong result on:\n"
              f"First sequence {seq1}\n"
              f"Second sequence {seq2}\n"
              f"Your answer is {provided_dels}, the correct answer is {correct_dels}")
        assert correct_dels == provided_dels


def levenshtein_substitution_correct(seq1, seq2):
    return sum([1 for a, b in zip(seq1, seq2) if a != b])


def levenshtein_deletions_correct(seq1, seq2):
    seq1, seq2 = sorted([seq1, seq2], reverse=True)
    max_allowed_deletions = len(seq1) - len(seq2)
    seq2 += "-" * (len(seq1) - len(seq2))

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

    return current_deletions


if __name__ == "__main__":
    levenshtein_deletions_correct("ATTT", "AT")