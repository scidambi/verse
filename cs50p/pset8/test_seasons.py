from seasons import input_to_date, age_minutes, age_minutes_to_words, age_days
from datetime import date
import pytest

def test_input_standard():
    assert input_to_date("1990-02-17") == date(1990, 2, 17)

def test_input_wrong_nonsense_date():
    with pytest.raises(SystemExit):
        input_to_date("1990-04303-923")

def test_input_wrong_format():
    with pytest.raises(SystemExit):
        input_to_date("February 17, 1990")

def test_input_wrong_month():
    with pytest.raises(SystemExit):
        input_to_date("1990-13-17")

def test_input_wrong_leap_year():
    with pytest.raises(SystemExit):
        input_to_date("2023-02-29")

def test_input_correct_leap():
    assert input_to_date("2024-02-29") == date(2024, 2, 29)

def test_age_minutes_to_words():
    assert age_minutes_to_words(1440) == "one thousand, four hundred forty"

def test_age_minutes():
    assert age_minutes(365) == 525600

def test_age_days_one_day():
    assert age_days(date(2026, 2, 27), date(2026, 2, 28)) == 1

def test_age_days_same_day():
    assert age_days(date(2026, 2, 27), date(2026, 2, 27)) == 0

def test_age_days_ten_day():
    assert age_days(date(2026, 2, 18), date(2026, 2, 28)) == 10

def test_age_days_two_day():
    assert age_days(date(2024, 2, 28), date(2024, 3, 1)) == 2

def test_age_days_one_day_no_leap():
    assert age_days(date(2023, 2, 28), date(2023, 3, 1)) == 1