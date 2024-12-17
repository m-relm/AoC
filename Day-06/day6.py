import copy

import numpy as np

def turn_guard(facing):
    # Defining the possible directions and their corresponding movement vectors
    directions = [
        ('Forward', (-1, 0)),   # Move up (row decreases)
        ('Right', (0, 1)),      # Move right (column increases)
        ('Downward', (1, 0)),   # Move down (row increases)
        ('Left', (0, -1))       # Move left (column decreases)
    ]

    # Find the index of the current facing direction
    current_index = next(i for i, (face, _) in enumerate(directions) if face == facing)

    # Get the next direction in the sequence
    next_index = (current_index + 1) % len(directions)  # Rotate forward with wrap-around
    new_facing, new_direction = directions[next_index]

    return new_facing, new_direction


# def move_guard(facing, direction):



def can_we_softlock_guard(patrol_grid, guard_position, guard_direction, guard_facing):
    # If we place an obstacle in front of the guard at this point in the grid, can we trap the guard
    # in an infinite loop where they can never reach the edge of the route?

    revised_grid = patrol_grid.copy()
    revised_guard = guard_position.copy()
    revised_direction = tuple(list(guard_direction))
    revised_facing = copy.copy(guard_facing)

    forward_obstacle = guard_position + guard_direction


    if test_guard_pathing(revised_grid, revised_guard, revised_direction, forward_obstacle, revised_facing):
        print("Guard is softlocked")
        return True
    return False

    # obstacle_spot = guard_position + guard_direction
#    revised_grid[guard_position[0], guard_position[1]] = '#'

def test_guard_pathing(revised_grid, guard_position, guard_direction, obstacle_spot, guard_facing):
    # If we place an obstacle at a specific point in the grid, can we trap the guard
    # in an infinite loop where they can never reach the edge

    revised_grid[obstacle_spot[0], obstacle_spot[1]] = '#'
    step_simulation = 18000
    softlocked_guard = True
    while step_simulation > 0:
        # print("Check for obstruction")
        obstruction_postion = guard_position + guard_direction
        obstruction_check = revised_grid[obstruction_postion[0], obstruction_postion[1]]

        if obstruction_check == "#":
            # print("Something in the way, turn right")
            guard_facing, guard_direction = turn_guard(guard_facing)
        elif obstruction_check == "E":
            print("End of the route")
            softlocked_guard = False
            break
        else:
            revised_grid[guard_position[0], guard_position[1]] = 'X'
            guard_position += guard_direction
        step_simulation -= 1
    return softlocked_guard


with open('./input-1.txt', 'r') as file:
    patrol_route = file.readlines()
    patrol_route = [list(route.strip()) for route in patrol_route]
    patrol_grid = np.array(patrol_route)

guard_spot = patrol_grid == 'G'
indices = np.argwhere(guard_spot)

guard_facing = 'Forward'
guard_direction = (-1, 0) # 'Forward'
guard_position = indices[0]

total_xs = 0
total_turns = 0
total_steps = 0
total_softlocks = 0
guard_in_bounds = True
patrol_grid[guard_position[0], guard_position[1]] = 'X'

while guard_in_bounds:
    obstruction_postion = guard_position + guard_direction
    obstruction_check = patrol_grid[obstruction_postion[0], obstruction_postion[1]]

    # print(guard_position)

    if obstruction_check == "#":
        total_turns += 1
        #guard_facing, guard_direction = turn_guard(guard_facing, guard_direction)
        guard_facing, guard_direction = turn_guard(guard_facing)
    elif obstruction_check == "E":
        print("End of the route")
        guard_in_bounds = False
        break
    else:
        # if obstruction_check == "X":
            # possible_softlock += 1
            # Didn't even need a carlbox
        print("Mark an X")
        total_steps += 1
        guard_position += guard_direction
        patrol_grid[guard_position[0], guard_position[1]] = 'X'
        if can_we_softlock_guard(patrol_grid, guard_position, guard_direction, guard_facing):
            total_softlocks += 1

    #guard_in_bounds = False

total_spots = (patrol_grid == 'X').sum()

total_obstacles = (patrol_grid == '#').sum()

var = True