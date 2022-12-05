import copy

import aoc_api


def solve():
    inputs = aoc_api.fetch_input(5)
    split_at = inputs.index('')
    (stacks, instructions) = get_stacks(inputs[:split_at - 1]), get_instructions(inputs[split_at + 1:])
    print("Final crates with crate mover 9000: " + get_top_row_of_stacks(move_crates_one_by_one(instructions, stacks)))
    print(
        "Final crates with crate mover 9100: " + get_top_row_of_stacks(move_three_crates_at_once(instructions, stacks)))


def get_top_row_of_stacks(stacks):
    return "".join([stack.pop() for stack in stacks])


def move_three_crates_at_once(instructions, input_stacks):
    stacks = copy.deepcopy(input_stacks)
    for instruction in instructions:
        moved_crates = [stacks[instruction[1] - 1].pop() for _ in range(instruction[0])]
        moved_crates.reverse()
        stacks[instruction[2] - 1].extend(moved_crates)
    return stacks


def move_crates_one_by_one(instructions, input_stacks):
    stacks = copy.deepcopy(input_stacks)
    for instruction in instructions:
        for _ in range(instruction[0]):
            stacks[instruction[2] - 1].append(stacks[instruction[1] - 1].pop())
    return stacks


def get_stacks(stack_sketch):
    stacks = [[line[i] for i in range(1, 34, 4)] for line in stack_sketch]
    stacks = list(zip(*stacks[::-1]))
    stacks = list(map(lambda stack: list(filter(lambda crate: crate != ' ', stack)), stacks))
    return stacks


def get_instructions(commands):
    instructions = [command.replace('move ', '').replace('from ', '').replace('to ', '').split() for command in
                    commands]
    return [list(map(int, instruction)) for instruction in instructions]
