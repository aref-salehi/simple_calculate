import pytest


def test_sum():
    assert function.sum(2,3) == 5
    assert function.sum(5,0) == 5
    assert function.sum(-2,3) == 1
    assert function.sum(3,-5) == -2
    