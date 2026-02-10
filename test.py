from script import sum, devide

def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a, b) == result


def test_devide():
    a = 4
    b = 2
    result = 2
    assert devide(a, b) == result

def test_deivision_prohibited():
    try:
        devide("A", "B")
        print("Test string division failed")
        assert False
    except ValueError as e:
        print("Test string division passed")

if __name__ == "__main__":
    test_sum()
    test_devide()
    test_deivision_prohibited()
    print("All tests passed")

