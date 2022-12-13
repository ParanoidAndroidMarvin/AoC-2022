import aoc_api

directions_straight = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
directions_diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
directions_all = directions_diagonal + list(directions_straight.values())


def solve():
    moves = aoc_api.fetch_input(9)
    print('Total amount of tail positions at length 2: {}'.format(trace_tail(moves, 2)))
    print('Total amount of tail positions at length 10: {}'.format(trace_tail(moves, 10)))


def trace_tail(moves, length):
    knots = [(0, 0)] * length
    tail_positions = set()
    for move in moves:
        (direction, distance) = move.split()
        for i in range(int(distance)):
            knots[0] = move_head(knots[0], direction)
            for j in range(1, length):
                new_position = move_tail(knots[j - 1], knots[j])
                if knots[j] == new_position:
                    break
                knots[j] = new_position
            tail_positions.add(knots[length - 1])
    return len(tail_positions)


def move_knot(knot, direction):
    return tuple(map(lambda a, b: a + b, knot, direction))


def move_head(head, direction):
    return move_knot(head, directions_straight[direction])


def move_tail(head, tail):
    if get_distance(head, tail) <= 1:
        return tail
    else:
        return get_best_position(head, tail, directions_all)


def get_best_position(head, tail, directions):
    possible_positions = map(lambda direction: move_knot(tail, direction), directions)
    possible_positions = [position for position in possible_positions if get_distance(head, position) <= 1]
    return next((position for position in possible_positions if sum(get_position_delta(head, position)) <= 1),
                possible_positions[0])


def get_distance(head, tail):
    delta = get_position_delta(head, tail)
    return sum(delta) - (0 if any(direction == 0 for direction in delta) else 1)


def get_position_delta(head, tail):
    return tuple(map(lambda a, b: abs(a - b), head, tail))
