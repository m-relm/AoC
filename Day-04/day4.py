import numpy as np
from setuptools.archive_util import unpack_directory

#When Part 2 doesn't work, make it all one line (line breaks are a PITA)

def look_for_xmas(start_x, start_y, direction, grid):
    x, y = start_x, start_y
    xmas = []
    for dx, dy in direction:
        new_x, new_y = x + dx, y + dy
        if new_y == 148:
            break
        if new_x == 148:
            break
        #print(f"{new_x} + {new_y}")
        xmas.append(grid[new_x, new_y])
        # if 0 <= new_x < grid.shape[0] and 0 <= new_y < grid.shape[1]:
        #     xmas.append(grid[new_x, new_y])

    if xmas == ['X', 'M', 'A', 'S']:
        return xmas

valid_grid_patterns = [
    ['M', 'B', 'M', 'B', 'A', 'B', 'S', 'B', 'S'],
    ['M', 'B', 'S', 'B', 'A', 'B', 'M', 'B', 'S'],
    ['S', 'B', 'S', 'B', 'A', 'B', 'M', 'B', 'M'],
    ['S', 'B', 'M', 'B', 'A', 'B', 'S', 'B', 'M'],
]

valid_patterns = {"SAM", "MAS"}

def look_for_grid_mas(initial_x, initial_y, direction, grid):
    x_start = max(0, initial_x - 1)
    x_end = min(grid.shape[0], initial_x + 2)
    y_start = max(0, initial_y - 1)
    y_end = min(grid.shape[1], initial_y + 2)

    scan_grid = grid[x_start:x_end, y_start:y_end]

    if scan_grid.shape == (3, 3):
        main_diagonal = [scan_grid[i, i] for i in range(3)]
        anti_diagonal = [scan_grid[i, 2 - i] for i in range(3)]

        if "".join(main_diagonal) in valid_patterns:
            if "".join(anti_diagonal) in valid_patterns:
                print(scan_grid)
                return True

    return False

    # x, y = start_x, start_y
    # xmas = []
    # for dx, dy in direction:
    #     new_x, new_y = x + dx, y + dy
    #     if new_y == 148:
    #         break
    #     if new_x == 148:
    #         break
    #     xmas.append(grid[new_x, new_y])

    # if start_x == 5:
    #     if start_y == 6:
    #         print(grid[start_x, start_y])
    #         var = True

    # xmas[1] = "B"
    # xmas[3] = "B"
    # xmas[5] = "B"
    # xmas[7] = "B"
    #
    # if xmas == any(valid_grid_patterns):
    #     print(f"Valid: {xmas}")
    #     return xmas
    # else:
    #     print(f"Invalid: {xmas}")

valid_mas_patterns = [
    ['M', 'A', 'S'],
    ['S', 'A', 'M'],
]

def look_for_mas_x(start_x, start_y, direction, grid):
    x, y = start_x, start_y
    xmas = []
    print(f"Start: {start_x}, {start_y} - {grid[start_x, start_y]}")
    for dx, dy in direction:
        new_x, new_y = x + dx, y + dy
        if new_y == 148:
            break
        if new_x == 148:
            break

        xmas.append(grid[new_x, new_y])

    if start_x == 5:
        if start_y == 6:
            var = True

    mas_1 = xmas[0:3]
    mas_2 = xmas[3:6]

    if mas_1[0] == 'M':
        if mas_1[1] == 'A':
            var = True


    if mas_1 == ['M', 'A', 'S']:
        var = True

    if mas_1 == any(valid_mas_patterns):
        print(f"Valid 1: {mas_1}")
        if mas_2 == any(valid_mas_patterns):
            print(f"Valid 2: {mas_2}")
            return xmas

    var = xmas[0:3] == ['M', 'A', 'S']

    print(xmas[0:3] == ['M', 'A', 'S'] or xmas[0:3] == ['S', 'A', 'M'])

    if xmas[0:3] == ['M', 'A', 'S'] or xmas[0:3] == ['S', 'A', 'M']:
        if xmas[3:6] == ['M', 'A', 'S'] or xmas[3:6] == ['S', 'A', 'M']:
            return xmas


with open('./input-1.txt', 'r') as file:
    read_lines = file.readlines()

parsed_lines = []
for line in read_lines:
    line = line.replace('\n', '')
    split_lines = []
    for character in line:
        split_lines.append(character)

    parsed_lines.append(split_lines)

xmas_grid = np.array(parsed_lines)

left_direction = [(-1, 0), (-2, 0), (-3, 0), (-4, 0)]
right_direction = [(1, 0), (2, 0), (3, 0), (4, 0)]
up_direction = [(0, -1), (0, -2), (0, -3), (0, -4)]
down_direction = [(0, 1), (0, 2), (0, 3), (0, 4)]
left_up_direction = [(-1, -1), (-2, -2), (-3, -3), (-4, -4)]
left_down_direction = [(-1, 1), (-2, 2), (-3, 3), (-4, 4)]
right_up_direction = [(1, -1), (2, -2), (3, -3), (4, -4)]
right_down_direction = [(1, 1), (2, 2), (3, 3), (4, 4)]

direction_map = [
    [(-1, 0), (-2, 0), (-3, 0), (-4, 0)],
    [(1, 0), (2, 0), (3, 0), (4, 0)],
    [(0, -1), (0, -2), (0, -3), (0, -4)],
    [(0, 1), (0, 2), (0, 3), (0, 4)],
    [(-1, -1), (-2, -2), (-3, -3), (-4, -4)],
    [(-1, 1), (-2, 2), (-3, 3), (-4, 4)],
    [(1, -1), (2, -2), (3, -3), (4, -4)],
    [(1, 1), (2, 2), (3, 3), (4, 4)],
]

# mas_pattern = [
#     (-1, -1), (1, 1), (1, 1), (-2, 0), (1, -1), (1, -1)
# ]

lets_select_a_grid = [
    (-1, -1), (0, 1), (0, 1), (1, -2), (0, 1), (0, 1), (1, -2), (0, 1), (0, 1)
]

xmas_cheer = 0
for x_coord in range(5, xmas_grid.shape[0]):
    for y_coord in range(5, xmas_grid.shape[1]):
        #for directions in direction_map:
            #xmas = look_for_xmas(x_coord, y_coord, directions, xmas_grid)
        xmas = look_for_grid_mas(x_coord, y_coord, lets_select_a_grid, xmas_grid)
        #xmas = look_for_mas_x(x_coord, y_coord, mas_pattern, xmas_grid)
        if xmas:
            print(f"Found XMAS at {x_coord}, {y_coord}")
            xmas_cheer += 1

print(parsed_lines)


