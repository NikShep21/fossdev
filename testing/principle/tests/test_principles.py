import sys

from math_demo import add, add_with_bug, calculate_tax_bugged, calculate_tax

def test_addition():
    assert add(2, 2) == 4
    assert add(3, 3) == 6
    print("Addition test passed.")
    
def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(3, 3) == 6
    print("Addition with bug test passed.")

def test_addition_duplicate():
    assert add(6, 7) == 6 + 7
    print("Addition duplicate test passed.")

def test_addition_overkill():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == i + j
            assert add(-i, -j) == -i + -j
            assert add(i, -j) == i + -j
            assert add(-i, j) == -i + j
    print("Addition overkill test passed.")

def test_addition_clussters():
    assert add(7,6) == 13
    assert add(8,9) == 17
    assert add(10,-11) == -1
    assert add(-12,-13) == -25
    assert add(-14,15) == 1
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    print("Addition clusters test passed.")

def test_addition_commutativity():
    assert add(5, 10) == 15
    assert add(10, 5) == 15
    assert add(-3, 7) == 4
    assert add(7, -3) == 4
    print("Addition commutativity test passed.")

def test_tax_calculator_bugged():
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15 
    assert calculate_tax_bugged(0) == 0
    assert calculate_tax_bugged(234) == 35.1
    print("Tax calculator test passed.")

def test_tax_calculator():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15 
    assert calculate_tax(0) == 0
    assert calculate_tax(234) == 35.1
    print("Tax calculator test passed.")

def test_negative_income():
    try:
        calculate_tax(-100)
        print("Negative income test failed.")
    except ValueError as e:
        assert str(e) == "Income cannot be negative"
        print("Negative income test passed.")

if __name__ == "__main__":
    test_addition()
    # test_addition_with_bug()
    test_addition_duplicate()
    # test_addition_overkill()
    test_addition_clussters()
    test_addition_commutativity()
    test_tax_calculator()
    test_tax_calculator_bugged()
    test_negative_income()

    