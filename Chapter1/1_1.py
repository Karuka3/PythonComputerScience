from typing import Dict, Generator
from functools import lru_cache
memo: Dict[int, int] = {0: 0, 1: 1}


def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n - 2) + fib1(n - 1)


def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 2) + fib2(n - 1)
    return memo[n]


@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n - 2) + fib3(n - 1)


def fib4(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next_: int = 1
    for _ in range(1, n):
        last, next_ = next_, last + next_
    return next_


def fib5(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next_: int = 1
    for _ in range(1, n):
        last, next_ = next_, last + next_
        yield next_


if __name__ == "__main__":
    for i in fib5(50):
        print(i)
