import pytest
from src.example import add, subtract

def test_add():
    assert add(1, 0) == 1
    assert add(1, 2) == 3
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(3, 1) == 2
    assert subtract(3, 3) == 0
    assert subtract(1, -1) == 0