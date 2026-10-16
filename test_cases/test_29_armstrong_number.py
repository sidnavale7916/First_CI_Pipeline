
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "29_armstrong_number.py"
)

spec = importlib.util.spec_from_file_location(
    "armstrong_number_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_armstrong = module.is_armstrong


def test_armstrong_number_153():
    assert is_armstrong(153) is True


def test_armstrong_number_370():
    assert is_armstrong(370) is True


def test_non_armstrong_number():
    assert is_armstrong(123) is False


def test_zero_is_armstrong():
    assert is_armstrong(0) is True


def test_negative_number():
    assert is_armstrong(-153) is False
