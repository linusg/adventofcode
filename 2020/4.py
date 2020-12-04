import sys
from typing import Dict, Iterable, List, Set

Passport = Dict[str, str]


def is_valid_passport(
    passport: Passport,
    *,
    strict_validation: bool,
    required_fields: Set[str] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"},
) -> bool:
    if bool((set(passport.keys()) ^ required_fields) & required_fields):
        return False
    if not strict_validation:
        return True
    valid = 1
    try:
        valid &= (byr := int(passport["byr"]), byr >= 1920 and byr <= 2002)[-1]
        valid &= (iyr := int(passport["iyr"]), iyr >= 2010 and iyr <= 2020)[-1]
        valid &= (eyr := int(passport["eyr"]), eyr >= 2020 and eyr <= 2030)[-1]
        valid &= (
            hgt := int(passport["hgt"][:-2]),
            hgt_unit := passport["hgt"][-2:],
            hgt >= {"cm": 150, "in": 59}[hgt_unit]
            and hgt <= {"cm": 193, "in": 76}[hgt_unit],
        )[-1]
        valid &= (
            hcl := passport["hcl"],
            int(hcl[1:], 16),
            len(hcl) == 7 and hcl[0] == "#",
        )[-1]
        valid &= passport["ecl"] in "amb blu brn gry grn hzl oth".split()
        valid &= (pid := passport["pid"], int(pid), len(pid) == 9)[-1]
    except (ValueError, KeyError):
        return False
    return bool(valid)


def parse(input_: str) -> List[Passport]:
    return [
        dict(pair.split(":") for pair in section.split())
        for section in input_.split("\n\n")
    ]


def solve_part1(passports: Iterable[Passport]) -> int:
    return sum(
        is_valid_passport(passport, strict_validation=False) for passport in passports
    )


def solve_part2(passports: Iterable[Passport]) -> int:
    return sum(
        is_valid_passport(passport, strict_validation=True) for passport in passports
    )


def main() -> None:
    input_ = sys.stdin.read()
    passports = parse(input_)
    print(solve_part1(passports))
    print(solve_part2(passports))


if __name__ == "__main__":
    main()
