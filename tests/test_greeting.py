# tests/test_greeting.py
import sys
import os

# flake8: noqa: E402  👈 Add this to tell flake8 to ignore import order in this file

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.greeting import get_greeting


def test_get_greeting():
    assert get_greeting("Betelhem") == "Hello, Betelhem!"
