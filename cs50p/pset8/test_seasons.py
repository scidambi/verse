from seasons import input_to_date
from datetime import date

def test_input_standard():
    assert input_to_date("1990-02-17") == date(1990, 2, 17)

def test_input_wrong_1():
    assert input_to_date("1990-04343-923") == "Invalid input"

def test_input_wrong_2():
    assert input_to_date("February 17, 1990") == SystemExit