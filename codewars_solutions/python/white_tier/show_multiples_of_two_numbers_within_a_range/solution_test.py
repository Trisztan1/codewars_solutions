from solution import multiples  # UNCHANGED

def test_multiples():  # MODIFIED: Replaced @test.describe with a standard Python function
    # MODIFIED: Replaced @test.it and test.assert_equals with standard assert statements
    assert multiples(2, 4, 40) == [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]  # MODIFIED
    assert multiples(3, 4, 40) == [12, 24, 36]  # MODIFIED
    assert multiples(7, 4, 80) == [28, 56]  # MODIFIED
    assert multiples(7, 4, 20) == []  # MODIFIED
    assert multiples(7, 5, 200) == [35, 70, 105, 140, 175]  # MODIFIED
    assert multiples(21, 5, 800) == [105, 210, 315, 420, 525, 630, 735]  # MODIFIED
    print("All tests passed successfully!")  # MODIFIED: Added success message

if __name__ == "__main__":  # MODIFIED: Added entry point to execute the tests
    test_multiples()  # MODIFIED
