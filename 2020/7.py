import re
import sys
from typing import Dict, List, Tuple

Rules = Dict[str, List[Tuple[str, int]]]


def bag_contains(target_bag_color: str, bag_color: str, rules: Rules) -> bool:
    if bag_color == target_bag_color:
        return True
    return any(
        bag_contains(target_bag_color, inner_bag_color, rules)
        for inner_bag_color, _ in rules[bag_color]
    )


def count_bags_containing(target_bag_color: str, rules: Rules) -> int:
    return sum(
        bag_contains(target_bag_color, bag_color, rules)
        for bag_color in rules
        if bag_color != target_bag_color
    )


def count_bags_in(bag_color: str, rules: Rules):
    return sum(
        count + count * count_bags_in(inner_bag_color, rules)
        for inner_bag_color, count in rules[bag_color]
    )


def solve_part1(rules: Rules) -> int:
    return count_bags_containing("shiny gold", rules)


def solve_part2(rules: Rules) -> int:
    return count_bags_in("shiny gold", rules)


def parse(input_: str) -> Rules:
    return {
        " ".join(line.split()[:2]): [
            (match[1], int(match[0]))
            for match in re.findall(r"(\d+) (\w+ \w+) bags?", line)
        ]
        for line in input_.splitlines()
    }


def main() -> None:
    input_ = sys.stdin.read()
    rules = parse(input_)
    print(solve_part1(rules))
    print(solve_part2(rules))


if __name__ == "__main__":
    main()
