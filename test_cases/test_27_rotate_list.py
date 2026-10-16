
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "27_rotate_list.py"
)

spec = importlib.util.spec_from_file_location(
    "rotate_list_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

rotate_list = module.rotate_list


def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_left():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_rotate_by_list_length():
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]


def test_rotate_empty_list():
    assert rotate_list([], 2) == []


def test_rotate_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]
