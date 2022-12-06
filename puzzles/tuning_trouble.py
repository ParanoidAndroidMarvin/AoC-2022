from queue import Queue

import aoc_api


def solve():
    datastream = aoc_api.fetch_input(6)[0]
    print("First 4 character marker appears at index: {}".format(get_first_marker(datastream, 4)))
    print("First 14 character marker appears at index: {}".format(get_first_marker(datastream, 14)))


def get_first_marker(datastream, marker_length):
    queue = Queue(maxsize=marker_length + 1)
    for i, character in enumerate(datastream):
        queue.put(character)
        if queue.full():
            queue.get()
            if len(set(queue.queue)) == marker_length:
                return i + 1
