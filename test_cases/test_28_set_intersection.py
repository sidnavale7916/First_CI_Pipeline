
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "28_set_intersection.py"
)

spec = importlib.util.spec_from_file_location(
    "set_intersection_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

set_intersection = module.set_intersection


def test_common_elements():
    assert set(set_intersection([1, 2, 3], [2, 3, 4])) == {2, 3}


def test_no_common_elements():
    assert set_intersection([1, 2], [3, 4]) == []


def test_identical_lists():
    assert set(set_intersection([1, 2, 3], [1, 2, 3])) == {1, 2, 3}


def test_empty_list():
    assert set_intersection([], [1, 2]) == []


def test_duplicates_are_removed():
    assert set(set_intersection([1, 1, 2, 2], [1, 1, 3])) == {1}
