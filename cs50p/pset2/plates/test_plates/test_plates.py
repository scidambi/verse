from plates import is_valid

def test_1():
    assert is_valid("AA1234") == True

def test_2():
    assert is_valid("121234") == False

def test_3():
    assert is_valid("A11234") == False

def test_4():
    assert is_valid("AAA234") == True

def test_5():
    assert is_valid("AA12345") == False

def test_6():
    assert is_valid("AA") == True

def test_7():
    assert is_valid("11") == False

def test_8():
    assert is_valid("1234567") == False

def test_9():
    assert is_valid("AA0234") == False

def test_10():
    assert is_valid("AA!234") == False

def test_11():
    assert is_valid("AA 234") == False

def test_12():
    assert is_valid("AABCDE") == True

def test_13():
    assert is_valid("AA12BC") == False