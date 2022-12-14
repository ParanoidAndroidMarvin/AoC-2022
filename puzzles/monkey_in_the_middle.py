import copy
import math

import aoc_api
import re


class Test:
    def __init__(self, instructions):
        self.divisor = int(re.search(r'\d+', instructions[0]).group())
        self.true = int(re.search(r'\d+', instructions[1]).group())
        self.false = int(re.search(r'\d+', instructions[2]).group())

    def get_result(self, worry_level):
        return self.true if worry_level % self.divisor == 0 else self.false


class Monkey:
    def __init__(self, instructions):
        self.items = list(map(int, instructions[1].split(': ')[1].split(', ')))
        self.operation = instructions[2].split(': ')[1].replace('new = ', '')
        self.test = Test(instructions[3:])
        self.inspections = 0

    def inspect_items(self, monkeys, relief_function):
        for item in self.items:
            self.inspections += 1
            worry_level = self.__calculate_worry_level(item)
            worry_level = relief_function(worry_level)
            monkeys[self.test.get_result(worry_level)].items.append(worry_level)
        self.items = []

    def __calculate_worry_level(self, old):
        return eval(self.operation.replace('old', str(old)))


def solve():
    puzzle_input = aoc_api.fetch_input(11) + ['']
    monkey_instructions = list(zip(*[iter(puzzle_input)] * 7))
    monkeys = list(map(Monkey, monkey_instructions))

    monkey_divisors = math.prod(map(lambda monkey: monkey.test.divisor, monkeys))
    print(play_keep_away(copy.deepcopy(monkeys), 20, lambda worry_level: worry_level // 3))
    print(play_keep_away(copy.deepcopy(monkeys), 10000, lambda worry_level: worry_level % monkey_divisors))


def play_keep_away(monkeys, rounds, reset_worry):
    for game_round in range(rounds):
        for monkey in monkeys:
            monkey.inspect_items(monkeys, reset_worry)
    monkey_inspections = list(map(lambda m: m.inspections, monkeys))
    return math.prod(sorted(monkey_inspections, reverse=True)[:2])
