import pytest
from solution import is_valid_walk  # Replace 'solution' with your module name


def test_valid_walk():
    assert is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is True


def test_walk_too_long():
    assert is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']) is False


def test_walk_too_short():
    assert is_valid_walk(['w']) is False


def test_walk_does_not_return_to_start():
    assert is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is False
