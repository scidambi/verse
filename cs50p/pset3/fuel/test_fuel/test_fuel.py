from fuel import convert
from fuel import gauge
import pytest


def test_none():
    with pytest.raises(ValueError):
        convert("0")
def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_quarter():
    assert convert("1/4") == 25
def test_half():
    assert convert("1/2") == 50
def test_whole():
    assert convert("1/1") == 100
def test_one_and_half():
    with pytest.raises(ValueError):
        convert("3/2")
def test_letters():
    with pytest.raises(ValueError):
        convert("a/b")


def test_gauge_empty():
    assert gauge(1.0) == "E"
def test_gauge_quarter():
    assert gauge(25) == "25%"
def test_gauge_half():
    assert gauge(55) == "55%"
def test_gauge_nearly_full():
    assert gauge(99.5) == "F"
