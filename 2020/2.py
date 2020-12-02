import re
import sys
from dataclasses import dataclass
from typing import Iterable, List

PASSWORD_AND_POLICY_REGEX = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


@dataclass
class PasswordAndPolicy:
    password: str
    character: str
    first_number: int
    second_number: int


def solve_part1(passwords_and_policies: Iterable[PasswordAndPolicy]) -> int:
    return sum(
        pap.password.count(pap.character) >= pap.first_number
        and pap.password.count(pap.character) <= pap.second_number
        for pap in passwords_and_policies
    )


def solve_part2(passwords_and_policies: Iterable[PasswordAndPolicy]) -> int:
    return sum(
        (
            pap.password[pap.first_number - 1] == pap.character
            and pap.password[pap.second_number - 1] != pap.character
        )
        or (
            pap.password[pap.first_number - 1] != pap.character
            and pap.password[pap.second_number - 1] == pap.character
        )
        for pap in passwords_and_policies
    )


def parse(input_: str) -> List[PasswordAndPolicy]:
    passwords_and_policies = []
    for line in input_.splitlines():
        match = PASSWORD_AND_POLICY_REGEX.match(line)
        assert match, "Regex did not match"
        groups = match.groups()
        passwords_and_policies.append(
            PasswordAndPolicy(
                password=groups[3],
                character=groups[2],
                first_number=int(groups[0]),
                second_number=int(groups[1]),
            )
        )
    return passwords_and_policies


def main() -> None:
    input_ = sys.stdin.read()
    passwords_and_policies = parse(input_)
    print(solve_part1(passwords_and_policies))
    print(solve_part2(passwords_and_policies))


if __name__ == "__main__":
    main()
