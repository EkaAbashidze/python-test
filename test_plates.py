from plates2 import is_valid

def test_zero():
    assert is_valid("0AAA123") == False
    
def test_symbols():
    assert is_valid("!ASDAQ312") == False
    
def test_length():
    assert is_valid("Abcd1") == False

def test_plates():
    assert is_valid("ABCD1234") == True