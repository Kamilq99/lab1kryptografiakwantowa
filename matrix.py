import numpy as np

# Definicja macierzy operatora M
M = np.array([[1, -1 + 1j, 1, -1 - 1j],
              [-1 + 1j, 1, -1 - 1j, 1],
              [1, -1 - 1j, 1, -1 + 1j],
              [-1 - 1j, 1, -1 + 1j, 1]])

print("Macierz operatora M:")
print(M)