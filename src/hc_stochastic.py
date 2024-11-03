from magic_utils import objective_function
import random

# Implementation of the Hill Climbing Stochastic algorithm
# @author: Rayhan Maheswara Pramanda
# @date: 2024-11-04

def hc_stochastic(cube, magic_number, max_iteration):
    n = cube.shape[0]

    # Initialise the current state value
    best_state_value = objective_function(cube, magic_number)

    for i in range(max_iteration):
        # Generate random indices for swapping two cells
        i, j, k = random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1)
        x, y, z = random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1)
        
        # Swap two cells
        cube[i, j, k], cube[x, y, z] = cube[x, y, z], cube[i, j, k]

        # Evaluate the candidate neighbour state value
        neighbour_state_value = objective_function(cube, magic_number)

        # Check the neighbour state value is better than the current best state value
        if neighbour_state_value < best_state_value:
            best_state_value = neighbour_state_value
        else:
            # Revert the swap
            cube[i, j, k], cube[x, y, z] = cube[x, y, z], cube[i, j, k]

    return cube, best_state_value
