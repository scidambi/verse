from fuel import convert
from fuel import gauge


def test_quarter():
    assert convert(0) == ""
def test_quarter():
    assert convert("1/4") == 25.0
def test_half():
    assert convert("1/2") == 50.0
def test_whole():
    assert convert("1/1") == 100.0

def test_gauge_empty():
    assert gauge(1.0) == "E"
def test_gauge_quarter():
    assert gauge(25.0) == "25.0%"
def test_gauge_half():
    assert gauge(55.0) == "55.0%"
def test_gauge_nearly_full():
    assert gauge(99.5) == "F"
