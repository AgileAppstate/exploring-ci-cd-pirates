# test_hello.py
from src.helloworld import get_message

def test_output():
    assert "Hello" in get_message()
