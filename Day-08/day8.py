from itertools import product

import numpy as np

def open_file(file_name):
    with open(f'./{file_name}', 'r') as file:
        cell_scans = file.readlines()
        cell_scans = [list(cell_scan.strip()) for cell_scan in cell_scans]
        cell_grid = np.array(cell_scans)
    return cell_grid


def find_towers(cell_grid, search_value):
    value_positions = np.where(cell_grid == search_value)
    positions_list = list(zip(value_positions[0], value_positions[1]))
    return positions_list
    # for each value returned, we need to form a matrix of all possible combinations of those values.


def generate_combinations(length, positions):
    return [
        combination for combination in product(positions, repeat=length)
        if len(set(combination)) == len(combination)
    ]


def find_antinodes(tower_combinations, cell_grid, antinode_grid):
    max_x = cell_grid.shape[0]
    max_y = cell_grid.shape[1]

    for combination in tower_combinations:
        offset_position = tuple(np.subtract(combination[0], combination[1]))
        point_antinode = tuple(np.add(combination[0], offset_position))
        antinode_grid[combination[0]] = 'X'

        keep_placing = True
        while keep_placing:
            if point_antinode[0] < 0 or point_antinode[1] < 0 or point_antinode[0] >= max_x or point_antinode[1] >= max_y:
                keep_placing = False
                continue

            antinode_grid[point_antinode[0], point_antinode[1]] = 'X'
            point_antinode = tuple(np.add(point_antinode, offset_position))


if __name__ == '__main__':
    cell_grid = open_file(file_name='input-1.txt')
    antinode_grid = np.full(cell_grid.shape, '.')

    search_values = list(np.unique(cell_grid))
    search_values.remove('.')

    for search_value in search_values:
        tower_positions = find_towers(cell_grid, search_value)
        tower_combinations = generate_combinations(2, tower_positions)

        find_antinodes(tower_combinations, cell_grid, antinode_grid)

    total_antinodes = (antinode_grid == 'X').sum()
    print(total_antinodes)
    var = True






