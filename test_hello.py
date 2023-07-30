from hello import hello

def test_hello():
    assert hello("Bitcamp") == "hello, Bitcamp"
    assert hello() == "hello, world"