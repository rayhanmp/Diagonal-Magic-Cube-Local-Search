from magic_utils import objective_function

# Implementation of the Hill Climbing with Sideways Move algorithm
# @author: Rayhan Maheswara Pramanda
# @date: 2024-11-03

def hc_sideways_move(cube, magic_number, max_sideways_moves): 
    n = cube.shape[0]

    # Initialise the current state value
    current_state_value = objective_function(cube, magic_number)
    best_state_value = current_state_value
    states = []
    states.append(cube.flatten())

    # Initialise the best cube as the initial cube
    best_cube = cube.copy()

    sideways_moves = 0

    while True:
        best_neighbour_state_value = current_state_value
        best_neighbour_swap = None

        # Iterate over the search space for swapping two cells
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for x in range(n):
                        for y in range(n):
                            for z in range(n):
                                if (i, j, k) != (x, y, z):
                                    # Swap two cells
                                    cube[i, j, k], cube[x, y, z] = cube[x, y, z], cube[i, j, k]

                                    # Evaluate the candidate neighbour state value
                                    neighbour_state_value = objective_function(cube, magic_number)

                                    # Check if this is the best swap so far
                                    if neighbour_state_value < best_neighbour_state_value:
                                        best_neighbour_state_value = neighbour_state_value
                                        best_neighbour_swap = (i, j, k), (x, y, z)

                                    # Revert the swap
                                    cube[i, j, k], cube[x, y, z] = cube[x, y, z], cube[i, j, k]

        # Check if a swap with better or equally good state value was found
        states.append(cube.flatten())
        if best_neighbour_swap and best_neighbour_state_value <= current_state_value:
            # Check if the best neighbour is better than the current state
            if best_neighbour_state_value < current_state_value:
                sideways_moves = 0  # Reset the counter
            else:
                sideways_moves += 1

            # End search if the maximum sideways moves has been reached
            if sideways_moves >= max_sideways_moves:
                break

            (i, j, k), (x, y, z) = best_neighbour_swap
            
            # Perform the best swap
            cube[i, j, k], cube[x, y, z] = cube[x, y, z], cube[i, j, k]
            current_state_value = best_neighbour_state_value

            if best_neighbour_state_value < best_state_value:
                best_state_value = best_neighbour_state_value
                best_cube = cube.copy()
        else:
            break

    return best_cube, best_state_value, states
