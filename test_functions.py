import pytest
import operations

def test_even_odd():
    assert opertions.check_even_odd(34) == "even"
    assert operations.check_even_odd(23) == "odd"
    

def test_factorial():
    assert operations.factorial(10) == 3628800
    assert operations.factorial(7) == 5040


def test_convert_temperature():
    assert operations.convert_temperature(25, C) == 77
    assert operations.convert_temperature(96, F) == 36

