import numpy as np
import random
import math
import time

# crossover method: Order Crossover (OX)
# mutation method: swapping between 2 element

start_time = time.time()
# define
max_iteration = 1000
cube_side = 5               # number of cube's side
max_population = 500       # max population number, GA start with max population
mutation_probability = 20   # probability of gene mutation base 100

def generate_random(N):
    # Calculate the total number of elements
    total_elements= N ** 3

    # Generate a list of integers from 1 to N^3
    numbers = list(range(1, total_elements + 1))

    # Shuffle the list to randomize the order of the integers
    random.shuffle(numbers)

    # Create a 3D matrix and fill it with the shuffled integers
    matrix_3d = np.zeros((N, N, N), dtype=int)

    index = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrix_3d[i][j][k] = numbers[index]
                index += 1

    return matrix_3d

def calculate_posibilities(population):
    possibilities = []
    max_value = 0

    for i in range(max_population):
        max_value += population[i][1]

    for i in range(max_population):
        value = math.floor(population[i][1]/max_value * 100)
        possibilities.append(value)

    return possibilities

# Fungsi untuk menghitung Magic Number untuk kubus n x n x n
def MagicNumber(n):
    return (n * (n**3 + 1)) // 2

# Fungsi untuk menghitung value dari suatu state kubus -> smaller better
def ObjectiveFunction(cube, magic_number):
    n = cube.shape[0]
    state_value = 0

    # Calculate difference for rows, columns, and depths
    for i in range(n):
        for j in range(n):
            # Sum across depth (z-axis), rows (y-axis), and columns (x-axis)
            state_value += abs(np.sum(cube[i, j, :]) - magic_number)
            state_value += abs(np.sum(cube[i, :, j]) - magic_number)
            state_value += abs(np.sum(cube[:, i, j]) - magic_number)

    # Calculate difference for face diagonals in each xy, xz, and yz plane
    for i in range(n):
        state_value += abs(np.sum(cube[i, range(n), range(n)]) - magic_number)
        state_value += abs(np.sum(cube[range(n), i, range(n)]) - magic_number)
        state_value += abs(np.sum(cube[range(n), range(n), i]) - magic_number)
        # Secondary diagonals
        state_value += abs(np.sum(cube[i, range(n), range(n-1, -1, -1)]) - magic_number)
        state_value += abs(np.sum(cube[range(n), i, range(n-1, -1, -1)]) - magic_number)
        state_value += abs(np.sum(cube[range(n-1, -1, -1), range(n), i]) - magic_number)

    # Calculate difference for 4 main space diagonals
    state_value += abs(np.sum(cube[range(n), range(n), range(n)]) - magic_number)
    state_value += abs(np.sum(cube[range(n), range(n), range(n-1, -1, -1)]) - magic_number)
    state_value += abs(np.sum(cube[range(n), range(n-1, -1, -1), range(n)]) - magic_number)
    state_value += abs(np.sum(cube[range(n-1, -1, -1), range(n), range(n)]) - magic_number)

    return state_value


# initial begin
max_number = cube_side ** 3
magicNumber = MagicNumber(cube_side)
new_population = []
all_population = []
for i in range(max_population):
    random_chromosom = generate_random(cube_side)
    chromosom_value = ObjectiveFunction(random_chromosom, magicNumber)
    if chromosom_value == 0:
        print("best possible case found when first generating\n")
        print(random_chromosom)
        SystemExit()
    new_population.append((random_chromosom, chromosom_value))
new_population = sorted(new_population, key=lambda x: x[1], reverse=False)

visualize_magic_cube(new_population[0][0], f"best of initialize iteration from {max_population} population(s) with value: {new_population[0][1]}")

print("best value at iteration 0 =", new_population[0][1])

for a in range(max_iteration):
    possibilities = calculate_posibilities(new_population)

    generation = []
    new_generation = []
    for i in range(max_population):
        roulete = random.randint(0, 100)
        value = 0
        for j in range(max_population):
            value += new_population[j][1]
            if (value <= roulete) or (j == (max_population - 1)):
                generation.append(new_population[j][0])
                break

    # crossover + mutation
    for i in range(0, max_population, 2):
        ## crossover
        #initiate
        crossover_point_min = random.randint(0, max_number - 1)
        crossover_point_max = random.randint(crossover_point_min, max_number - 1)

        parent_1 = generation[i].flatten()
        parent_2 = generation[i + 1].flatten()

        child_1 = np.zeros((max_number), dtype=int)
        child_2 = np.zeros((max_number), dtype=int)

        child_1 -= 1
        child_2 -= 1

        #child 1
        child_1[crossover_point_min : crossover_point_max] = parent_1[crossover_point_min : crossover_point_max]
        pointer_parent = crossover_point_max
        pointer_child = crossover_point_max
        for j in range(max_number):
            if parent_2[pointer_parent] not in child_1:
                child_1[pointer_child] = parent_2[pointer_parent]
                pointer_child = (pointer_child + 1) % (max_number)

            pointer_parent = (pointer_parent + 1) % (max_number)

        #child 2
        child_2[crossover_point_min : crossover_point_max] = parent_2[crossover_point_min : crossover_point_max]
        pointer_parent = crossover_point_max
        pointer_child = crossover_point_max
        for j in range(max_number):
            if parent_1[pointer_parent] not in child_2:
                child_2[pointer_child] = parent_1[pointer_parent]
                pointer_child = (pointer_child + 1) % (max_number)

            pointer_parent = (pointer_parent + 1) % (max_number)

        ## mutation
        # does child 1 mutate?
        roulete = random.randint(0, 100)
        if roulete < mutation_probability:
            mutation_point_1 = random.randint(0, max_number - 1)
            mutation_point_2 = random.randint(0, max_number - 1)

            # Swap the elements in the flattened array
            child_1[mutation_point_1], child_1[mutation_point_2] = child_1[mutation_point_2], child_1[mutation_point_1]

        # does child 2 mutate?
        roulete = random.randint(0, 100)
        if roulete < mutation_probability:
            mutation_point_1 = random.randint(0, max_number - 1)
            mutation_point_2 = random.randint(0, max_number - 1)

            # Swap the elements in the flattened array
            child_2[mutation_point_1], child_2[mutation_point_2] = child_2[mutation_point_2], child_2[mutation_point_1]

        # insert to new generation
        new_generation.append(child_1.reshape((cube_side, cube_side, cube_side)))
        new_generation.append(child_2.reshape((cube_side, cube_side, cube_side)))


    for i in range(max_population):
        chromosom_value = ObjectiveFunction(new_generation[i], magicNumber)

        if chromosom_value == 0:
            print("best possible case found in", a, "iteration\n")
            print(new_generation[i])
            SystemExit()

        all_population.append((new_generation[i], chromosom_value))

    # add the old population
    all_population += new_population

    all_population = sorted(all_population, key=lambda x: x[1], reverse=False)

    new_population = all_population[0:max_population]

    # print("best value at iteration", a, "=", new_population[0][1])

finish_time = time.time()
elapsed_time = finish_time - start_time

print(f"After {max_iteration} iteration(s) in {elapsed_time:.6f} second(s) resulting in its best value of {new_population[0][1]} (smaller better). The magic cube is as follows:\n")
print(new_population[0][0]) #print as matrix

visualize_magic_cube(new_population[0][0], f"best last iteration with value: {new_population[0][1]}")
