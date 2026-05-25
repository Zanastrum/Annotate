from plates import is_valid

def test_length():
    assert is_valid("TooLong") == False
    assert is_valid("T") == False
    assert is_valid("TS") == True
    assert is_valid("Exact") == True

def test_order():
    assert is_valid("1CDEFG") == False
    assert is_valid("CDE1FG") == False
    assert is_valid("CDEFG1") == True

def test_punctuation():
    assert is_valid("DDD.") == False
    assert is_valid("DotD") == True

def test_digits():
    assert is_valid("123") == False
    assert is_valid("1CD") == False
    assert is_valid("CD1") == True

def test_zeroes():
    assert is_valid("CD01") == False
    assert is_valid("CD10") == True
