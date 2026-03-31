from calc import add, multiply, subtract


def test_add_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_add_negative_and_positive() -> None:
    assert add(-1, 1) == 0


def test_subtract_numbers() -> None:
    assert subtract(10, 4) == 6


def test_multiply_numbers() -> None:
    assert multiply(6, 7) == 42
