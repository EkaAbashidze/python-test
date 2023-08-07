from bank2 import value

def test_hello():
    assert value("Hello") == 0
    
def test_h():
    assert value("Hola") == 20

def test_str():
    assert value("Ciao") == 100