from os import system

import keyboard

from puzzles import calorie_counting, rock_paper_scissors, rucksack_reorganization, camp_cleanup, supply_stacks

selected = 1
puzzles = [
    "Calorie Counting",
    "Rock Paper Scissors",
    "Rucksack Reorganization",
    "Camp Cleanup",
    "Supply Stacks"
]


def clear():
    system('clear')


def show_menu():
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
    global selected
    selected = max(1, selected - 1)
    show_menu()


def down():
    global selected
    selected = min(len(puzzles), selected + 1)
    show_menu()


def select():
    print('\n\nPuzzle result day {0}:'.format(selected))
    print('---------------------------')
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


show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('left', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', down)
keyboard.add_hotkey('enter', select)
keyboard.add_hotkey('backspace', show_menu)
keyboard.wait('esc')
