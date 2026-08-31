import pytest
from solution import create_phone_number


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "(111) 111-1111"),
        ([0, 2, 3, 0, 5, 6, 0, 8, 9, 0], "(023) 056-0890"),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "(000) 000-0000"),
    ],
)
def test_create_phone_number(input_array, expected_output):
    assert create_phone_number(input_array) == expected_output
