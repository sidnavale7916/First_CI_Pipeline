
import importlib.util
from pathlib import Path

module_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "30_decimal_to_binary.py"
)

spec = importlib.util.spec_from_file_location(
    "decimal_to_binary_module", module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

decimal_to_binary = module.decimal_to_binary


def test_decimal_to_binary_10():
    assert decimal_to_binary(10) == "1010"


def test_decimal_to_binary_7():
    assert decimal_to_binary(7) == "111"


def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "0"


def test_decimal_to_binary_2():
    assert decimal_to_binary(2) == "10"


def test_negative_number_raises_value_error():
    try:
        decimal_to_binary(-5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for a negative number"
