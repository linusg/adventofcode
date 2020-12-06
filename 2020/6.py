import sys
from typing import Iterable, List


def solve_part1(quiz_answers: Iterable[Iterable[str]]) -> int:
    return sum(len(set("".join(group_answers))) for group_answers in quiz_answers)


def solve_part2(quiz_answers: Iterable[Iterable[str]]) -> int:
    return sum(
        len(
            set(
                c
                for answer in group_answers
                for c in answer
                if all(c in answer for answer in group_answers)
            )
        )
        for group_answers in quiz_answers
    )


def parse(input_: str) -> List[List[str]]:
    return [group.splitlines() for group in input_.split("\n\n")]


def main() -> None:
    input_ = sys.stdin.read()
    quiz_answers = parse(input_)
    print(solve_part1(quiz_answers))
    print(solve_part2(quiz_answers))


if __name__ == "__main__":
    main()
