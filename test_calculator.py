import pytest
from calculator import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(3, 5) == 8
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(10, 4) == 6
    assert restar(0, 1) == -1

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(5, 0) == 0

def test_dividir():
    assert dividir(8, 2) == 4
    with pytest.raises(ValueError):
        dividir(5, 0)
