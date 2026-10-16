
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "24_merge_sorted_lists.py"
)

spec = importlib.util.spec_from_file_location(
    "merge_sorted_lists_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

merge_sorted_lists = module.merge_sorted_lists


def test_merge_two_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_different_lengths():
    assert merge_sorted_lists([1, 5], [2, 3, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_with_empty_list():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_merge_both_empty_lists():
    assert merge_sorted_lists([], []) == []


def test_merge_lists_with_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 3]) == [1, 2, 2, 2, 3, 3]
