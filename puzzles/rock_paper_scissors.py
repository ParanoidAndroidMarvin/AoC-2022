import aoc_api

# a/y - Rock
# b/x - Paper
# c/z - Scissors


move_scores = {'A': 1, 'B': 2, 'C': 3}
move_wins = {'A': 'B', 'B': 'C', 'C': 'A'}
move_loss = {'A': 'C', 'B': 'A', 'C': 'B'}


def solve():
    moves = aoc_api.fetch_input(2)
    print('Total game score part 1: ' + str(solve_part1(moves)))
    print('Total game score part 2: ' + str(solve_part2(moves)))


def solve_part1(moves):
    total_score = 0
    for move in moves:
        (opponent, me) = move.split()
        me = me.replace('X', 'A').replace('Y', 'B').replace('Z', 'C')
        total_score += get_game_score(opponent, me)
        total_score += move_scores[me]
    return total_score


def solve_part2(moves):
    total_score = 0
    for move in moves:
        (opponent, result) = move.split()

        me = ''
        match result:
            case 'X':
                me = move_loss[opponent]
            case 'Y':
                me = opponent
            case 'Z':
                me = move_wins[opponent]

        total_score += get_game_score(opponent, me)
        total_score += move_scores[me]
    return total_score


def game_wins(opponent, me):
    return me == move_wins[opponent]


def get_game_score(opponent, me):
    if opponent == me:
        return 3
    elif game_wins(opponent, me):
        return 6
    return 0
