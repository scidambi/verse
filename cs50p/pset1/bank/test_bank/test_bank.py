from bank import value_greeting

def test_1():
    assert value_greeting("hello") == 0

def test_2():
    assert value_greeting("hey") == 20

def test_3():
    assert value_greeting("yo") == 100

def test_4():
    assert value_greeting("hello there") == 0

def test_empty():
    assert value_greeting("") == 100

def test_leading_spaces():
    assert value_greeting(" hello") == 0