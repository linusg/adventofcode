import sys
from math import floor, ceil
from typing import Iterable, Tuple


def resolve_position_in_range(start: int, end: int, chars: str) -> int:
    r = [start, end]
    for c in chars:
        if c in ("F", "L"):
            r[1] = r[0] + floor((r[1] - r[0]) / 2)
        elif c in ("B", "R"):
            r[0] = r[1] + ceil((r[0] - r[1]) / 2)
        else:
            assert False, f"Invalid character '{c}'"
    assert r[0] == r[1], "Not enough steps to resolve single position"
    return r[0]


def parse_seat_location(line: str) -> Tuple[int, int]:
    return (
        resolve_position_in_range(0, 127, line[:7]),
        resolve_position_in_range(0, 7, line[7:10]),
    )


def get_seat_id(seat_location: Tuple[int, int]) -> int:
    row, column = seat_location
    return row * 8 + column


def solve_part1(boarding_list: Iterable[int]) -> int:
    return max(boarding_list)


def solve_part2(boarding_list: Iterable[int]) -> int:
    seat_ids = sorted(boarding_list)
    for i in range(1, len(seat_ids)):
        if seat_ids[i] + 1 not in seat_ids:
            return seat_ids[i] + 1
        if seat_ids[i] - 1 not in seat_ids:
            return seat_ids[i] - 1
    assert False, "Couldn't determine missing seat ID from boarding list"


def main() -> None:
    input_ = sys.stdin.read()
    boarding_list = [
        get_seat_id(parse_seat_location(line)) for line in input_.splitlines()
    ]
    print(solve_part1(boarding_list))
    print(solve_part2(boarding_list))


if __name__ == "__main__":
    main()
