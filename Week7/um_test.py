from test import count

def test():
    assert count("um") == 1
    assert count("album") == 0
    assert count("Um, thanks, um...") == 2
