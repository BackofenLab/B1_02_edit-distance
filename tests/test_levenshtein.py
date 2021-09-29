import pytest
from sheet_2 import levenshtein


@pytest.mark.parametrize(
    "seq1,seq2,expected",
    [
        ("AGATATA", "TATATATA", 2),
        ("AGTCCT", "CGCTCA", 4),
        ("TGCATAT", "ATCCGAT", 4),
        ("ATCCGAT", "TGCATAT", 4),
        ("", "", 0),
        ("A", "", 1),
     ]
)
def test_levenstein(seq1, seq2, expected):
    test = levenshtein(seq1, seq2)
    assert test == expected
