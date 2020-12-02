import sys
from itertools import combinations
from functools import reduce
from operator import mul
from typing import Iterable


def solve(expense_report: Iterable[int], *, combinations_count: int) -> int:
    for values in combinations(expense_report, combinations_count):
        if sum(values) == 2020:
            return reduce(mul, values, 1)
    raise RuntimeError("No solution could be found!")


def main() -> None:
    input_ = sys.stdin.read()
    expense_report = [int(line) for line in input_.splitlines()]
    print(solve(expense_report, combinations_count=2))
    print(solve(expense_report, combinations_count=3))


if __name__ == "__main__":
    main()
