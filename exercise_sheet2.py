def exercise_1():
    """
    Compute the minimal Levenshtein edit distance for the following pairs of sequences.
    """

    #S1= "", S2= ""
    a = None

    #S1= "A", S2= ""
    b = None

    #S1= "AGATATA", S2= "TATATATA"
    c = None

    #S1= "AGTCCT", S2= "CGCTCA"
    d = None

    #S1= "TGCATAT", S2= "ATCCGAT"
    e = None

    #S1= "ATCCGAT", S2= "TGCATAT"
    f = None

    return a, b, c, d, e, f


def exercise_2():
    """
    In order to enable an appropriate scoring of edit operations, the cost
    function has to be a metric.
    +
    Are the following cost functions w : (R +0 , R 0 ) → R metrics?
    """

    #w(x, y) = x - y
    a = None

    #w(x, y) = |x - y|
    b = None

    #w(x, y) = x + y
    c = None

    #w(x, y) = 1 if x != y else 0
    d = None

    return a, b, c, d


########################################################
############## Programming tasks #######################
########################################################


def levenshtein_substitution(sequence1, sequence2):
    number_substitutions = None
    return number_substitutions


def levenshtein_deletions(sequence1, sequence2):
    deletions_indexes = None
    return deletions_indexes
