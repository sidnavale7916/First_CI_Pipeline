
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "26_sum_of_list.py"
)

spec = importlib.util.spec_from_file_location(
    "sum_of_list_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

sum_of_list = module.sum_of_list


def test_sum_positive_numbers():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_sum_negative_numbers():
    assert sum_of_list([-1, -2, -3]) == -6


def test_sum_mixed_numbers():
    assert sum_of_list([-2, 5, 3]) == 6


def test_sum_empty_list():
    assert sum_of_list([]) == 0


def test_sum_single_number():
    assert sum_of_list([7]) == 7
