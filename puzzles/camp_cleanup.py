import aoc_api


def solve():
    assignments = aoc_api.fetch_input(4)

    contained_sections = 0
    overlapping_sections = 0
    for assignments in assignments:
        (assignment1, assignment2) = assignments.split(',')
        (range1, range2) = get_range(assignment1), get_range(assignment2)
        if sections_are_contained(range1, range2):
            contained_sections += 1
        if sections_overlap(range1, range2):
            overlapping_sections += 1

    print(str(contained_sections) + ' assignments are contained within one another!')
    print(str(overlapping_sections) + ' sections are overlapping!')


def sections_overlap(section1, section2):
    return len(set(section1).intersection(section2)) != 0


def sections_are_contained(range1, range2):
    return all(section in range1 for section in range2) or all(section in range2 for section in range1)


def get_range(section):
    (start, end) = section.split('-')
    return range(int(start), int(end) + 1)
