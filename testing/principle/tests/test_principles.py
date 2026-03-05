import sys

from math_demo import add, add_with_bug

def test_addition():
    assert add(2, 2) == 4
    assert add(3, 3) == 6
    print("Addition test passed.")
    
def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(3, 3) == 6
    print("Addition with bug test passed.")
    

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()