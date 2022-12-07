from os import system
import keyboard
import time

from puzzles import calorie_counting, rock_paper_scissors, rucksack_reorganization, camp_cleanup, supply_stacks, \
    tuning_trouble, no_space_left_on_device

selected = 1
in_menu = True
puzzles = [
    "Calorie Counting",
    "Rock Paper Scissors",
    "Rucksack Reorganization",
    "Camp Cleanup",
    "Supply Stacks",
    "Tuning Trouble",
    "No Space Left On Device"
]


def clear():
    system('clear')


def show_menu():
    global in_menu
    in_menu = True

    clear()
    print('AdventOfCode')
    print('=================')
    print('Choose puzzle:')
    for i in range(1, len(puzzles) + 1):
        print('{2} Day {0}: {1} {3}'.format(i,
                                            puzzles[i - 1],
                                            ">" if selected == i else " ",
                                            "<" if selected == i else " "))
    print('\n[˄]Up [˅]Down [return]Select [esc]Exit')


def up():
    if in_menu:
        global selected
        selected = max(1, selected - 1)
        show_menu()


def down():
    if in_menu:
        global selected
        selected = min(len(puzzles), selected + 1)
        show_menu()


def select():
    global in_menu
    if not in_menu:
        return
    in_menu = False

    clear()
    print('Puzzle result day {0}:'.format(selected))
    print('---------------------------')

    start = time.time()
    match selected:
        case 1:
            calorie_counting.solve()
        case 2:
            rock_paper_scissors.solve()
        case 3:
            rucksack_reorganization.solve()
        case 4:
            camp_cleanup.solve()
        case 5:
            supply_stacks.solve()
        case 6:
            tuning_trouble.solve()
        case 7:
            no_space_left_on_device.solve()
    stop = time.time()
    print('\nExecution time: {}s'.format(round(stop-start, 3)))
    print('\n[<--]Show Menu [esc]Exit')


show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('left', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', down)
keyboard.add_hotkey('enter', select)
keyboard.add_hotkey('backspace', show_menu)
keyboard.wait('esc')
