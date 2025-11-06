# tests/test_greeting.py
import sys
import os

# ✅ Add the absolute path to your project root (1 level up)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.greeting import get_greeting


def test_get_greeting():
    assert get_greeting("Betelhem") == "Hello, Betelhem!"
