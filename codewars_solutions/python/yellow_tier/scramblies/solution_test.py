import pytest
from solution import scramble


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("rkqodlw", "world", True),
        ("cedewaraaossoqqyt", "codewars", True),
        ("katas", "steak", False),
        ("scriptjava", "javascript", True),
        ("scriptingjava", "javascript", True),
    ],
)
def test_scramble_basic(s1, s2, expected):
    assert scramble(s1, s2) == expected, f"Failed with\ns1 = \"{s1}\"\ns2 = \"{s2}\""


def test_scramble_large_input():
    s1 = "abcdefghijklmnopqrstuvwxyz" * 10_000
    s2 = "zyxcba" * 9_000
    assert scramble(s1, s2) is True, f"Failed large test with\ns1 len = {len(s1)}\ns2 len = {len(s2)}"
