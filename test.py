import pytest


def test_sum():
    assert function.add(2,3) == 5
    assert function.add(5,0) == 5
    assert function.add(-2,3) == 1
    assert function.add(3,-5) == -2
    