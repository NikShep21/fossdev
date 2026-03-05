from tax.income import calculate_tax

def test_income_tax():
    assert calculate_tax(1000) == 150.00
    assert calculate_tax(0) == 0.00
    assert calculate_tax(1234.56) == 185.18
    print("Income tax tests passed!")

if __name__ == "__main__":
    test_income_tax()

