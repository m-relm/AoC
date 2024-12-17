import numpy as np

# Create a grid (example)
grid = [
    ['c', 'a', 't'],
    ['a', 't', 'o'],
    ['t', 'o', 'p']
]

# Convert list of lists to a numpy array for easy manipulation
grid_array = np.array(grid)


def get_neighbors(x, y, grid):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    neighbors = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < grid.shape[0] and 0 <= new_y < grid.shape[1]:
            neighbors.append(grid[new_x, new_y])

    return neighbors


# Example: Get neighbors of the element at position (1, 1)
x, y = 1, 1
neighbors = get_neighbors(x, y, grid_array)
print("Neighbors of element at (1, 1):", neighbors)
