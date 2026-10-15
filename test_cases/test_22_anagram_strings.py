
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "22_anagram_strings.py"
)

spec = importlib.util.spec_from_file_location(
    "anagram_strings_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_anagram = module.is_anagram


def test_anagram_basic():
    assert is_anagram("listen", "silent") is True


def test_anagram_different_case():
    assert is_anagram("Listen", "Silent") is True


def test_anagram_with_spaces():
    assert is_anagram("Dormitory", "Dirty room") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_empty_strings():
    assert is_anagram("", "") is True
