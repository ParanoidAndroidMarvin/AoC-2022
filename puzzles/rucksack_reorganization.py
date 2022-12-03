import aoc_api


def solve():
    rucksacks = aoc_api.fetch_input(3)
    print('Total item priority: ' + str(solve_part1(rucksacks)))
    print('Total batch priority: ' + str(solve_part2(rucksacks)))


def solve_part1(rucksacks):
    total_priority = 0
    for rucksack in rucksacks:
        (compartment1, compartment2) = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        item_type = set(compartment1).intersection(compartment2).pop()
        total_priority += get_priority(item_type)
    return total_priority


def solve_part2(rucksacks):
    total_priority = 0
    groups = list(zip(*[iter(rucksacks)] * 3))
    for group in groups:
        badge = set(group[0]).intersection(group[1], group[2]).pop()
        total_priority += get_priority(badge)
    return total_priority


def get_priority(item_type):
    return ord(item_type) - (38 if item_type.isupper() else 96)
