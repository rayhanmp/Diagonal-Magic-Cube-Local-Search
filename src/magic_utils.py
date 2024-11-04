import numpy as np

# Module for basic magic-cube-related utilities
# @author: Rayhan Maheswara Pramanda & Jasmine Callista Aurellie Irfan
# @date: 2024-11-04

# Determine Magic Number for N Cube
def magic_number(n):
    return (n * (n**3 + 1)) // 2

# Make a 3D cube with random unique numbers from 1..N^3
def make_cube(n):
    cube = np.arange(1, n**3 + 1)
    np.random.shuffle(cube)
    return cube.reshape((n, n, n))

# Objective function for calculating a magic cube state value
def objective_function(cube, magic_number):
    n = cube.shape[0]
    state_value = 0

    # Calculate difference for depth, rows, and columns
    for i in range(n):
        for j in range(n):
            state_value += abs(np.sum(cube[i, j, :]) - magic_number)
            state_value += abs(np.sum(cube[i, :, j]) - magic_number)
            state_value += abs(np.sum(cube[:, i, j]) - magic_number)

    # Calculate difference for face diagonals in each xy, xz, and yz plane
    for i in range(n):
        # Main diagonals
        state_value += abs(np.sum(cube[i, range(n), range(n)]) - magic_number)
        state_value += abs(np.sum(cube[range(n), i, range(n)]) - magic_number)
        state_value += abs(np.sum(cube[range(n), range(n), i]) - magic_number)

        # Opposite diagonals
        state_value += abs(np.sum(cube[i, range(n), range(n-1, -1, -1)]) - magic_number)
        state_value += abs(np.sum(cube[range(n), i, range(n-1, -1, -1)]) - magic_number)
        state_value += abs(np.sum(cube[range(n-1, -1, -1), range(n), i]) - magic_number)

    # Calculate difference for all the space diagonals
    state_value += abs(np.sum(cube[range(n), range(n), range(n)]) - magic_number)
    state_value += abs(np.sum(cube[range(n), range(n), range(n-1, -1, -1)]) - magic_number)
    state_value += abs(np.sum(cube[range(n), range(n-1, -1, -1), range(n)]) - magic_number)
    state_value += abs(np.sum(cube[range(n-1, -1, -1), range(n), range(n)]) - magic_number)

    return state_value

# Write states to file
def write_states_to_file(states, filename):
    np.savez(filename, states)

# Read states from file
def read_states_from_file(filename):
    with np.load(filename) as data:
        states = [data[key] for key in data]
    return states

# Test driver
def test_magic_cube(cube):
    n = cube.shape[0]
    mc = magic_number(n)
    state_value = objective_function(cube, mc)

    # Expected value for the test cube
    expected_value = 186
    assert state_value == expected_value, f"Expected {expected_value}, but the function returned {state_value} instead."

# Define the test cube
test_cube = np.array([
    [[8, 24, 10],
     [12, 7, 23],
     [22, 11, 9]],

    [[15, 1, 26],
     [25, 14, 3],
     [2, 27, 13]],

    [[19, 17, 6],
     [5, 21, 16],
     [18, 4, 20]]
])

# Run the test driver
test_magic_cube(test_cube)