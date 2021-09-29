

def levenshtein(sequence1: str, sequence2: str) -> int:
    """ Calculate the Levenshtein Distance of two strings
    Fill this function such that it calculates the levenshtein distance of
    the two strings sequence1 and sequence2. The return value is supposed to be
    an integer.
    """
    return None


def exercise_2():
    """
    In order to enable an appropriate scoring of edit operations, the cost
    function has to be a metric.
    +
    Are the following cost functions w : (R +0 , R 0 ) → R metrics?
    """

    "w(x, y) = x - y"
    a = None

    "w(x, y) = |x - y|"
    b = None

    "w(x, y) = x + y"
    c = None

    "w(x, y) = 1 if x != y else 0"
    d = None

    return a, b, c, d
