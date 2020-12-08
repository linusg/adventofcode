import sys
from itertools import chain
from typing import Iterator, List, Sequence, Tuple

Instruction = Tuple[str, int]  # name, value
ExecutionResult = Tuple[int, bool]  # accumulator, did_terminate


def execute(instructions: Sequence[Instruction]) -> ExecutionResult:
    accumulator = 0
    instruction_pointer = 0
    executed_instructions = set()
    while (
        instruction_pointer not in executed_instructions
        and instruction_pointer < len(instructions)
    ):
        executed_instructions.add(instruction_pointer)
        name, value = instructions[instruction_pointer]
        if name == "acc":
            accumulator += value
            instruction_pointer += 1
        if name == "jmp":
            instruction_pointer += value
        if name == "nop":
            instruction_pointer += 1
    return accumulator, instruction_pointer >= len(instructions)


def swap_instructions(
    instructions: Sequence[Instruction], old_name: str, new_name: str
) -> Iterator[List[Instruction]]:
    for i, instruction in enumerate(instructions):
        name, value = instruction
        if name != old_name:
            continue
        new_instructions = list(instructions)
        new_instructions[i] = (new_name, value)
        yield new_instructions


def solve_part1(instructions: Sequence[Instruction]) -> int:
    accumulator, _ = execute(instructions)
    return accumulator


def solve_part2(instructions: Sequence[Instruction]) -> int:
    for new_instructions in chain(
        swap_instructions(instructions, "nop", "jmp"),
        swap_instructions(instructions, "jmp", "nop"),
    ):
        accumulator, did_terminate = execute(new_instructions)
        if did_terminate:
            return accumulator
    assert False, "Couldn't get the program to terminate"


def parse(input_: str) -> List[Instruction]:
    return [(line.split()[0], int(line.split()[1])) for line in input_.splitlines()]


def main() -> None:
    input_ = sys.stdin.read()
    instructions = parse(input_)
    print(solve_part1(instructions))
    print(solve_part2(instructions))


if __name__ == "__main__":
    main()
