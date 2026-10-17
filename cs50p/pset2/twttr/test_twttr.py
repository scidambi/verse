from twttr import shorten


def test_twttr_upper():
    assert shorten("HOWIE") == "HW"

def test_twttr_capital():
    assert shorten("Howie") == "Hw"

def test_twttr_lower():
    assert shorten("howie") == "hw"

def test_twttr_all_vowels():
    assert shorten("aeiou") == ""

def test_twttr_all_vowels_upper():
    assert shorten("AEIOU") == ""

def test_twttr_all_consonants():
    assert shorten("hw") == "hw"

def test_twttr_numbers():
    assert shorten("123") == "123"

def test_twttr_punct():
    assert shorten("o'meara!") == "'mr!"

def test_twttr_empty():
    assert shorten("") == ""




