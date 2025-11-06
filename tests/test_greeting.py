import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


def test_get_greeting():
    from src.greeting import get_greeting  # local import ✅
    assert get_greeting("Betelhem") == "Hello, Betelhem!"
