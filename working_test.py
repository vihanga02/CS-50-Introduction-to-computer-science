from test import convert
import pytest

def testing():
    #testing valied inputs
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

    #testing invalied inputs
    assert convert("9AM - 5PM") == "Invalied"
    assert convert("09:00 to 17:00") == "Invalied"
