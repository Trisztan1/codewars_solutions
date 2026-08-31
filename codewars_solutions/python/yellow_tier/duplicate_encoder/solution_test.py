import pytest
from solution import duplicate_encode


@pytest.mark.parametrize(
    "word, expected",
    [
        ("din", "((("),
        ("recede", "()()()"),
        ("Success", ")())())"),
        ("(( @", "))(("),
    ],
    ids=["all_unique", "repeated_letters", "case_insensitive", "special_chars"],
)
def test_duplicate_encode(word, expected):
    assert duplicate_encode(word) == expected
