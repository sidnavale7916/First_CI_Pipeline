
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "21_largest_word.py"
)

spec = importlib.util.spec_from_file_location(
    "largest_word_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

largest_word = module.largest_word


def test_largest_word_basic():
    assert largest_word("Python is amazing") == "amazing"


def test_largest_word_single_word():
    assert largest_word("Hello") == "Hello"


def test_largest_word_empty_sentence():
    assert largest_word("") == ""


def test_largest_word_multiple_spaces():
    assert largest_word("I love programming") == "programming"


def test_largest_word_equal_length():
    assert largest_word("cat dog") == "cat"
