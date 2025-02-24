import pytest

from hellobencher import fib


@pytest.mark.parametrize(
    "n, expected_result",
    [
        [0, 0],
        [1, 1],
        [2, 1],
        [3, 2],
        [4, 3],
        [5, 5],
        [10, 55],
    ],
)
def test_fib(n, expected_result):
    assert fib(n) == expected_result


def benchmark_fib(benchmark):
    benchmark(lambda: fib(20))
