from magic_utils import objective_function
import numpy as np
import math

# Implementasi Algoritma Simulated Annealing
def simulated_annealing(cube, magicNumber, temperature, cooling_rate, iterations, threshold):
    n = cube.shape[0]
    current_cube = cube.copy()
    current_score = objective_function(current_cube, magicNumber)
    best_cube = current_cube.copy()
    best_score = current_score

    states = []
    states.append(cube.flatten())

    for _ in range(iterations):
        # Pilih dua posisi acak untuk ditukar
        i, j, k = np.random.randint(0, n, size=3)
        x, y, z = np.random.randint(0, n, size=3)

        # Tukar elemen terpilih
        current_cube[i, j, k], current_cube[x, y, z] = current_cube[x, y, z], current_cube[i, j, k]

        # Hitung nilai objective function baru
        new_score = objective_function(current_cube, magicNumber)

        # Hitung delta E dan probabilitas
        delta_E = current_score - new_score
      
        # Metropolis acceptance criterion
        probability = math.exp(min(max(delta_E / temperature, -700), 700)) # Dibatasi untuk rentang [-700, 700] untuk menghidari overflow error
        states.append(cube.flatten())

        # Tentukan apakah menerima state baru
        if delta_E > 0 or probability > threshold:
            current_score = new_score
            if new_score < best_score:
                best_cube = current_cube.copy()
                best_score = new_score
        else:
            # Kembalikan ke kondisi sebelumnya jika tidak diterima
            current_cube[i, j, k], current_cube[x, y, z] = current_cube[x, y, z], current_cube[i, j, k]

        # Kurangi temperatur
        temperature *= cooling_rate

    return best_cube, best_score, states
