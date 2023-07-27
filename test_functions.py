from numpy import true_divide
import pytest
import operations

def test_even_odd():
    assert check_even_odd(34) == "even"
    assert check_even_odd(23) == "odd"
    pass
    

def test_factorial():
    assert factorial(10) == 3628800
    assert factorial(7) == 5040
    pass


def test_convert_temperature():
    assert convert_temperature(25, C) == 77
    assert convert_temperature(96, F) == 35.55
    pass

