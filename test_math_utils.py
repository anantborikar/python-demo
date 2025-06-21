from math_utils import add, subtract

def test_add():
    assert add(2, 4) == 6
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 2) == 0
