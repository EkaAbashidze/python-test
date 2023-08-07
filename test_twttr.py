from twttr import shorten

def test_twttr():
    assert shorten("TWITTER") == "twttr"
    assert shorten("Twitter") == "twttr"
    assert shorten("twitter") == "twttr"
    assert shorten("Eka") == "k"
    assert shorten("") == ""