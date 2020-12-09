import sys
from itertools import combinations
from typing import List, Sequence


def find_invalid_number(numbers: Sequence[int], *, preamble_length: int) -> int:
    for i in range(preamble_length, len(numbers)):
        preamble = numbers[i - preamble_length : i]
        number = numbers[i]
        valid_numbers = {sum(pair) for pair in combinations(preamble, 2)}
        if number not in valid_numbers:
            return number
    assert False, "All numbers seem to be valid!"


def find_contiguous_range(numbers: Sequence[int], *, expected_sum: int) -> List[int]:
    for i in range(len(numbers) - 2):
        # Speed up the brute-forcing a bit.
        if numbers[i] > expected_sum:
            continue
        for j in range(i, len(numbers) - 1):
            # Speed up the brute-forcing a bit more.
            if numbers[j] > expected_sum or (numbers[i] + numbers[j]) > expected_sum:
                continue
            if sum(numbers[i:j]) == expected_sum:
                return list(numbers[i:j])
    assert False, f"No contiguous range of numbers could be found!"


def solve_part1(numbers: Sequence[int]) -> int:
    return find_invalid_number(numbers, preamble_length=25)


def solve_part2(numbers: Sequence[int]) -> int:
    invalid_number = solve_part1(numbers)
    contiguous_range = find_contiguous_range(numbers, expected_sum=invalid_number)
    return min(contiguous_range) + max(contiguous_range)


def parse(input_: str) -> List[int]:
    return [int(line) for line in input_.splitlines()]


def main() -> None:
    input_ = sys.stdin.read()
    numbers = parse(input_)
    print(solve_part1(numbers))
    print(solve_part2(numbers))


if __name__ == "__main__":
    main()
