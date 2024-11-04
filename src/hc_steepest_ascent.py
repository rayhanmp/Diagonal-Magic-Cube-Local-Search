from magic_utils import objective_function

# Implementation of the Hill Climbing Steepest Ascent algorithm
# @author: Rayhan Maheswara Pramanda
# @date: 2024-11-03

def hc_steepest_ascent(cube, magic_number):
    n = cube.shape[0]
    num_of_iteration = 0

    # Initialise the current state value
    current_state_value = objective_function(cube, magic_number)
    best_state_value = current_state_value

    # Initialise the best cube as the initial cube
    best_cube = cube.copy()

    while True:
        num_of_iteration += 1
        best_neighbour_state_value = current_state_value
        best_neighbour_swap = None

        # Iterate over the search space for swapping two cells
        # TODO: Optimize search algorithm complexity or use parallel processing
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

        # Check if a better swap was found
        if best_neighbour_swap and best_neighbour_state_value < current_state_value:
            (i, j, k), (x, y, z) = best_neighbour_swap
            
            # Perform the best swap
            cube[i, j, k], cube[x, y, z] = cube[x, y, z], cube[i, j, k]
            current_state_value = best_neighbour_state_value

            if best_neighbour_state_value < best_state_value:
                best_state_value = best_neighbour_state_value
                best_cube = cube.copy()
        else:
            break

    return best_cube, best_state_value, num_of_iteration
