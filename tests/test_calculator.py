# tests/test_calculator.py

import pytest
from src.calculator import Calculator

def test_add():
    assert Calculator.add(3, 2) == 5
    assert Calculator.add(-1, 1) == 0

def test_subtract():
    assert Calculator.subtract(3, 2) == 1
    assert Calculator.subtract(2, 3) == -1
