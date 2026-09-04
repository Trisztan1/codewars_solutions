import pytest
# Import your function implementation from solution.py
# (Handles both camelCase and snake_case naming conventions)
try:
    from solution import removNb as remov_nb
except ImportError:
    from solution import remov_nb


@pytest.mark.parametrize(
    "n, expected",
    [
        (26, [(15, 21), (21, 15)]),
        (100, []),
        (101, [(55, 91), (91, 55)]),
    ],
)
def test_remov_nb(n, expected):
    assert remov_nb(n) == expected
