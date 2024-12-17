from itertools import product

import numpy as np

def open_file(file_name):
    with open(f'./{file_name}', 'r') as file:
        # the_file = file.readline()
        the_file = file.readlines()
        # the_file = list(the_file.strip())
        the_file = [list(file_part.strip()) for file_part in the_file]
        file_grid = np.array(the_file)

    # return the_file
    return file_grid


def find_trailheads(topographical_map):
    trail_heads = []
    for x_coord in range(len(topographical_map)):
        for y_coord in range(len(topographical_map[x_coord])):
            if topographical_map[x_coord][y_coord] == '0':
                trail_heads.append((x_coord, y_coord))

    return trail_heads

def check_and_validate_position(trail_head, direction, topographical_map):
    check_position = (trail_head[0] + direction[1][0], trail_head[1] + direction[1][1])

    if check_position[0] < 0 or check_position[1] < 0:
        return False, check_position
    if check_position[0] >= len(topographical_map) or check_position[1] >= len(topographical_map[0]):
        return False, check_position

    return int(topographical_map[check_position]), check_position

directions = [
        ('Forward', (-1, 0)),  # Move up (row decreases)
        ('Right', (0, 1)),  # Move right (column increases)
        ('Downward', (1, 0)),  # Move down (row increases)
        ('Left', (0, -1))  # Move left (column decreases)
    ]

def new_blaze_meta_dropped(the_map, current_position, compare_value: int, score: int, pathway: list[str], scoring_trails: list[tuple[int, int]]):
    for direction in directions:
        check_value, new_position = check_and_validate_position(current_position, direction, the_map)
        if check_value == compare_value:

            if check_value == 9:
                print(f"{pathway} {check_value} {direction[0]}")
                scoring_trails.append(new_position)
                score += 1
            else:
                pathway.append(f"{check_value} {direction[0]}")
                score, scoring_trails = new_blaze_meta_dropped(the_map, new_position, compare_value + 1, score, pathway, scoring_trails)
                pathway.pop()
    return score, scoring_trails




def blaze_the_trail(topographical_map, trail_heads):
    directions = [
        ('Forward', (-1, 0)),   # Move up (row decreases)
        ('Right', (0, 1)),      # Move right (column increases)
        ('Downward', (1, 0)),   # Move down (row increases)
        ('Left', (0, -1))       # Move left (column decreases)
    ]

    topographical_score = 0
    unique_trails = 0
    for trail_head in trail_heads:
        trail_score, scoring_trails = new_blaze_meta_dropped(topographical_map, trail_head, 1, 0, ["0"], [])
        topographical_score += len(set(scoring_trails))
        unique_trails += len(scoring_trails)
        print(topographical_score)
        # for direction_1 in directions:
        #     check_value, new_position = check_and_validate_position(trail_head, direction_1, topographical_map)
        #     if check_value == '1':
        #         for direction_2 in directions:
        #             check_value, check_position = check_and_validate_position(new_position, direction_2, topographical_map)
        #             # print(f"2: {check_value}")
        #             if check_value == '2':
        #                 new_position = check_position
        #                 for direction_3 in directions:
        #                     check_value, check_position = check_and_validate_position(new_position, direction_3, topographical_map)
        #                     # print(f"3: {check_value}")
        #                     if check_value == '3':
        #                         new_position = check_position
        #                         for direction_4 in directions:
        #                             check_value, check_position = check_and_validate_position(new_position, direction_4,
        #                                                                       topographical_map)
        #                             # print(f"4: {check_value}")
        #                             if check_value == '4':
        #                                 new_position = check_position
        #                                 for direction_5 in directions:
        #                                     check_value, check_position = check_and_validate_position(new_position, direction_5,
        #                                                                               topographical_map)
        #                                     # print(f"5: {check_value}")
        #                                     if check_value == '5':
        #                                         new_position = check_position
        #                                         for direction_6 in directions:
        #                                             check_value, check_position = check_and_validate_position(new_position, direction_6,
        #                                                                                       topographical_map)
        #                                             # print(f"6: {check_value}")
        #                                             if check_value == '6':
        #                                                 new_position = check_position
        #                                                 for direction_7 in directions:
        #                                                     check_value, check_position = check_and_validate_position(new_position,
        #                                                                                               direction_7,
        #                                                                                               topographical_map)
        #                                                     print(f"7: {check_value}")
        #                                                     if check_value == '7':
        #                                                         new_position = check_position
        #                                                         for direction_8 in directions:
        #                                                             check_value, check_position = check_and_validate_position(
        #                                                                 new_position,
        #                                                                 direction_8,
        #                                                                 topographical_map)
        #                                                             print(f"8: {check_value}")
        #                                                             if check_value == '8':
        #                                                                 new_position = check_position
        #                                                                 for direction_9 in directions:
        #                                                                     check_value, check_position = check_and_validate_position(
        #                                                                         new_position,
        #                                                                         direction_9,
        #                                                                         topographical_map)
        #                                                                     print(f"9: {check_value}")
        #                                                                     if check_value == '9':
        #                                                                         topographical_score += 1
        #                                                                         print("We Found a Peak!")


    return unique_trails #topographical_score


if __name__ == '__main__':
    topographical_map = open_file(file_name='input-1.txt')

    trail_heads = find_trailheads(topographical_map)
    evaluation_score = blaze_the_trail(topographical_map, trail_heads)

    print(f"We Scored: {evaluation_score}")

    #paths = calculate_paths('input-0.txt')

    var = True