import pytest
from tax.income import calculate_tax

def test_calculate_tax():
    assert calculate_tax(1000) == 130.00

def test_calculate_tax_integer_cents():
    assert calculate_tax(1234.56) == 160.49

@pytest.mark.parametrize("income, expected", [
    (1000, 130.00),
    (1234.56, 160.49)
])
def test_calculate_tax_parametrized(income, expected):
    assert calculate_tax(income) == expected