import aoc_api


def solve():
    program = aoc_api.fetch_input(10)
    cycle = 0
    current_signal_strength = 1
    total_signal_strength = 0
    crt_display = [''] * 6

    for command in program:
        cycle += 1
        total_signal_strength = check_signal_strength(cycle, current_signal_strength, total_signal_strength)
        crt_display = draw_pixel(cycle, current_signal_strength, crt_display)
        if command.startswith('addx'):
            cycle += 1
            total_signal_strength = check_signal_strength(cycle, current_signal_strength, total_signal_strength)
            crt_display = draw_pixel(cycle, current_signal_strength, crt_display)
            current_signal_strength += int(command.split()[1])

    print('Total signal strength: {}'.format(total_signal_strength))
    print('CRT display:')
    for line in crt_display:
        print(line)


def check_signal_strength(cycle, current, total):
    if (cycle - 20) % 40 == 0:
        return total + (cycle * current)
    return total


def draw_pixel(cycle, current, display):
    row = (cycle - 1) // 40
    column = (cycle - 1) % 40
    display[row] += '#' if column - 1 <= current <= column + 1 else '.'
    return display


solve()
