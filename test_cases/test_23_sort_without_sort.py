
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "23_sort_without_sort.py"
)

spec = importlib.util.spec_from_file_location(
    "sort_without_sort_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

bubble_sort = module.bubble_sort


def test_sort_unsorted_list():
    assert bubble_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_sort_already_sorted_list():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_sort_reverse_order():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_sort_empty_list():
    assert bubble_sort([]) == []


def test_sort_does_not_change_original():
    numbers = [3, 1, 2]
    bubble_sort(numbers)
    assert numbers == [3, 1, 2]
