

"""
Exercise 1 - Levenshtein Distance

- Compute the minimal Levenshtein edit distance for the following pairs of
  sequences.
- The response should be an integer value.

"""


def exercise_1a():
    """
    S1= "A", S2= ""
    """
    return None


def exercise_1b():
    """
    S1= "AGATATA", S2= "TATATATA"
    """
    return None


def exercise_1c():
    """
    S1= "AGTCCT", S2= "CGCTCA"
    """
    return None


def exercise_1d():
    """
    S1= "TGCATAT", S2= "ATCCGAT"
    """
    return None


def exercise_1e():
    """
    S1= "ATCCGAT", S2= "TGCATAT"
    """
    return None


"""
Exercise 2 - Metric function

- Check if the corresponding functions are metric.
- The respond should be a boolean value (True or False)

"""


def exercise_2a():
    """
    w(x, y) = x - y
    """
    return None


def exercise_2b():
    """
    w(x, y) = |x - y|
    """
    return None


def exercise_2c():
    """
    w(x, y) = x + y
    """
    return None


def exercise_2d():
    """
    w(x, y) = 1 if x != y else 0
    """
    return None


"""
Exercise 3 - Programming assignment: Levenshtein Distance

- Implement the corresponding function

"""


def levenshtein_substitution(sequence1, sequence2):
    """
    Implement the function levenshtein_substitution() which takes two sequences
    of the same length and computes the minimum number of substitutions to
    transform one into another.
    """
    number_substitutions = None
    return number_substitutions


def levenshtein_deletions(sequence1, sequence2):
    """
     Implement the function levenshtein_deletion() which takes two sequences
     of different length and returns the positions of characters from the
     longest sequences which should be deleted to transform the sequence into
     the other one. If such deletion can not be done the function should
     return None.
    """
    deletions_indexes = None
    return deletions_indexes