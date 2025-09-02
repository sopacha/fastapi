import pytest
from app.calculations import add

@pytest.mark.parametrize("num1, num2, expected", [(2, 3, 5)])

def test_add(num1, num2, expected):
    assert add (num1, num2) == expected