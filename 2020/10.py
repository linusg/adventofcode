import sys
from collections import defaultdict
from typing import DefaultDict, List, Sequence


def get_rating_differences(adapter_ratings: Sequence[int]) -> DefaultDict[int, int]:
    adapter_ratings_sorted = sorted(adapter_ratings)
    rating_differences: DefaultDict[int, int] = defaultdict(int)
    for i, rating in enumerate(adapter_ratings_sorted):
        rating_differences[rating - (adapter_ratings_sorted[i - 1] if i else 0)] += 1
    # built-in adapter is always 3 higher than the highest adapter
    rating_differences[3] += 1
    return rating_differences


def get_possible_arrangements_count(adapter_ratings: Sequence[int]) -> int:
    adapter_ratings_sorted = sorted(adapter_ratings)
    combinations_up_to: DefaultDict[int, int] = defaultdict(int)
    combinations_up_to[0] = 1
    for rating in adapter_ratings_sorted:
        combinations_up_to[rating] = (
            combinations_up_to[rating - 1]
            + combinations_up_to[rating - 2]
            + combinations_up_to[rating - 3]
        )
    # built-in adapter can't increase number of possible combinations
    return combinations_up_to[adapter_ratings_sorted[-1]]


def solve_part1(adapter_ratings: Sequence[int]) -> int:
    differences = get_rating_differences(adapter_ratings)
    return differences[1] * differences[3]


def solve_part2(adapter_ratings: Sequence[int]) -> int:
    return get_possible_arrangements_count(adapter_ratings)


def parse(input_: str) -> List[int]:
    return [int(line) for line in input_.splitlines()]


def main() -> None:
    input_ = sys.stdin.read()
    adapter_ratings = parse(input_)
    print(solve_part1(adapter_ratings))
    print(solve_part2(adapter_ratings))


if __name__ == "__main__":
    main()
