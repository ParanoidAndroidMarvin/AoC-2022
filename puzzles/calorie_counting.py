import aoc_api


def solve():
    calories = aoc_api.fetch_input(1)
    total_calories = [0]

    for calorie in calories:
        if calorie == '':
            total_calories.append(0)
        else:
            total_calories[-1] += int(calorie)

    print('Elf carrying the most calories: ' + str(max(total_calories)))
    print('Top 3 calories in total: ' + str(sum(sorted(total_calories, reverse=True)[:3])))
