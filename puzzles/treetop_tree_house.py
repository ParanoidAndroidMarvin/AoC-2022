import aoc_api
import numpy as np
from functools import reduce


def solve():
    tree_map = np.array(aoc_api.fetch_input(8), dtype=bytes)
    tree_map = tree_map.view('S1').reshape((tree_map.size, -1)).astype(int)
    print('Total trees visible: {}'.format(solve_part1(tree_map)))
    print('Highest scenic score: {}'.format(solve_part2(tree_map)))


def solve_part1(tree_map):
    visible_trees = 0
    for x, y in np.ndindex(tree_map.shape):
        if is_edge(x, y, tree_map) or is_visible(x, y, tree_map):
            visible_trees += 1
    return visible_trees


def is_edge(x, y, tree_map):
    return not 0 < x < tree_map.shape[0] - 1 or not 0 < y < tree_map.shape[1] - 1


def is_visible(x, y, tree_map):
    height = tree_map[x, y]
    row = tree_map[x, :]
    column = tree_map[:, y]
    return any(max(trees) < height for trees in (row[:y], row[y+1:], column[:x], column[x+1:]))


def solve_part2(tree_map):
    scenic_scores = []
    for x, y in np.ndindex(tree_map.shape):
        if is_edge(x, y, tree_map):
            continue
        height = tree_map[x, y]
        row = tree_map[x, :]
        column = tree_map[:, y]
        directions = (np.flip(row[:y]), row[y+1:], np.flip(column[:x]), column[x+1:])
        viewing_distances = list(map(lambda direction: get_viewing_distance(height, direction), directions))
        scenic_scores.append(reduce(lambda a, b: a*b, viewing_distances))
    return max(scenic_scores)


def get_viewing_distance(max_height, trees):
    return next((index+1 for index, height in enumerate(trees) if height >= max_height), len(trees))
