import pytest
from src.app import calculate_discount


def test_calculate_discount():
    assert calculate_discount(1000, 10) == 900


def test_no_discount():
    assert calculate_discount(1000, 0) == 1000


def test_full_discount():
    assert calculate_discount(1000, 100) == 0


def test_invalid_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(1000, 110)