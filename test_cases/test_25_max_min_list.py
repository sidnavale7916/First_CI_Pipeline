
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "25_max_min_list.py"
)

spec = importlib.util.spec_from_file_location(
    "max_min_list_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_max_min = module.find_max_min


def test_positive_numbers():
    assert find_max_min([3, 1, 9, 5]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-5, -2, -10]) == (-2, -10)


def test_single_number():
    assert find_max_min([7]) == (7, 7)


def test_duplicate_numbers():
    assert find_max_min([4, 2, 4, 2]) == (4, 2)


def test_empty_list_raises_value_error():
    try:
        find_max_min([])
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError for an empty list"
