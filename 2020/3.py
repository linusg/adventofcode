import sys
from functools import reduce
from operator import mul
from typing import Iterator, Tuple


def traverse_map_and_count_trees(map_: str, *, x_step: int, y_step: int) -> int:
    lines = map_.splitlines()

    def coordinates() -> Iterator[Tuple[int, int]]:
        x, y = 0, 0
        while y < len(lines) - y_step:
            yield (x := x + x_step), (y := y + y_step)

    return [lines[y][x % len(lines[y])] for x, y in coordinates()].count("#")


def solve_part1(map_: str) -> int:
    return traverse_map_and_count_trees(map_, x_step=3, y_step=1)


def solve_part2(map_: str) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [traverse_map_and_count_trees(map_, x_step=x, y_step=y) for x, y in slopes]
    return reduce(mul, trees, 1)


def main() -> None:
    input_ = sys.stdin.read()
    print(solve_part1(input_))
    print(solve_part2(input_))


if __name__ == "__main__":
    main()
