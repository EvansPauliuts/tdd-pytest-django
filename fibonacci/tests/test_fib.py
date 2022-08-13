import pytest

from typing import Callable
from fibonacci.my_decorator import my_parametrized
from fibonacci import naive, cached
from fixtures import time_tracker


@my_parametrized(identifiers="n,expected", values=[(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fib_naive(n: int, expected: int) -> None:
    res = naive.fibonacci_naive(n=n)
    assert res == expected


@pytest.mark.parametrize(
    "fib_func",
    [naive.fibonacci_naive, cached.fibonacci_cached, cached.fibonacci_lru_cached],
)
@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_cached(
    time_tracker, fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    res = fib_func(n)
    assert res == expected
