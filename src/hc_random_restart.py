from magic_utils import objective_function
from hc_steepest_ascent import hc_steepest_ascent
import numpy as np

# Implementation of the Hill Climbing with Random Restart algorithm
# @author: Rayhan Maheswara Pramanda
# @date: 2024-11-04

def hc_random_restart(cube, magic_number, max_restarts):
    num_of_restart = 0
    num_of_iterations = []

    # Initialise the best state value and cube
    best_state_value = objective_function(cube, magic_number)
    best_cube = cube.copy()

    # Repeat the random restart for n times
    while (num_of_restart < max_restarts):
        # Randomly shuffle the cube
        np.random.shuffle(cube)

        cube, state_value, num_of_iteration = hc_steepest_ascent(cube, magic_number)

        num_of_iterations.append(num_of_iteration)

        # Update the best state value
        if state_value < best_state_value:
            best_state_value = state_value
            best_cube = cube.copy()
        
        num_of_restart += 1

    return best_cube, best_state_value, num_of_iterations