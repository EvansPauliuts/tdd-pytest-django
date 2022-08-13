# import pytest

from fibonacci.my_decorator import my_parametrized
from fibonacci.naive import fibonacci_naive


# @pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
@my_parametrized(identifiers="n,expected", values=[(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fib_naive(n: int, expected: int) -> None:
    res = fibonacci_naive(n=n)
    assert res == expected
