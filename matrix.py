import numpy as np

# Definicja macierzy operatora M
M = np.array([[1, -1 + 1j, 1, -1 - 1j],
              [-1 + 1j, 1, -1 - 1j, 1],
              [1, -1 - 1j, 1, -1 + 1j],
              [-1 - 1j, 1, -1 + 1j, 1]])

print("Macierz operatora M:")
print(M)

# a) Znajdź wartości własne λ macierzy M
eigenvalues, eigenvectors = np.linalg.eig(M)
print("\nWartości własne λ macierzy M:")
print(eigenvalues)

# b) Znajdź odpowiadające im wektory własne ψλ
print("\nOdpowiadające im wektory własne ψλ:")
for i, eigenvector in enumerate(eigenvectors.T):
    print(f"λ_{i+1}: {eigenvector}")

# c) Skonstruuj odpowiadające im macierze gęstości ρλ
density_matrices = [np.outer(eigenvector, np.conj(eigenvector)) for eigenvector in eigenvectors.T]
print("\nOdpowiadające im macierze gęstości ρλ:")
for i, density_matrix in enumerate(density_matrices):
    print(f"ρ_{i+1}:")
    print(density_matrix)
    print()
