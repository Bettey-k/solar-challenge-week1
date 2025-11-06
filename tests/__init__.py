# tests/test_greeting.py
from src.greeting import get_greeting

def test_get_greeting():
    assert get_greeting("Betelhem") == "Hello, Betelhem!"
    assert "Hello" in get_greeting("AI")
