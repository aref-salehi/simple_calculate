import pytest
import functions as function

def test_sum():
    assert function.add(2,3) == 5
    assert function.add(5,0) == 5
    assert function.add(-2,3) == 1
    assert function.add(3,-5) == -2
    
def test_subtract():
    assert function.subtract(1,3) == -2
    assert function.subtract(2,2) == 0
    assert function.subtract(3,-4) == 7
    assert function.subtract(-5,9) == -14
    
    