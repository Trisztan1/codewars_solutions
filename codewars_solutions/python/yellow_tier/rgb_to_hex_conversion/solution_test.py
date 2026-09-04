import pytest
from solution import rgb


@pytest.mark.parametrize(
    "r, g, b, expected, message",
    [
        (0, 0, 0, "000000", "testing zero values"),
        (1, 2, 3, "010203", "testing near zero values"),
        (255, 255, 255, "FFFFFF", "testing max values"),
        (254, 253, 252, "FEFDFC", "testing near max values"),
        (-20, 275, 125, "00FF7D", "testing out of range values"),
    ],
)
def test_rgb(r, g, b, expected, message):
    assert rgb(r, g, b) == expected, message
