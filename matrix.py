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

# Własności rozwiązań
print("Własności rozwiązań:")
for i, rho in enumerate(density_matrices):
    print(f"\nρ_{i+1}:")
    # a) Sprawdź czy ρ jest samosprzężone
    print(f"a) Czy ρ_{i+1} jest samosprzężone? {np.allclose(rho, np.conj(rho.T))}")
    
    # b) Sprawdź czy ρ jest dodatnio określone
    print(f"b) Czy ρ_{i+1} jest dodatnio określone? {np.all(np.linalg.eigvals(rho) > 0)}")
    
    # c) Sprawdź idempotyczność ρ^2 = ρ
    rho_squared = np.dot(rho, rho)
    print(f"c) Czy ρ^2_{i+1} = ρ_{i+1}? {np.allclose(rho_squared, rho)}")
    
    # d) Oblicz ślady Tr(ρ) oraz Tr(ρ^2)
    trace_rho = np.trace(rho)
    trace_rho_squared = np.trace(rho_squared)
    print(f"d) Ślady Tr(ρ_{i+1}) oraz Tr(ρ^2_{i+1}): {trace_rho}, {trace_rho_squared}")
    print("   Ślady reprezentują sumę prawdopodobieństw danego stanu kwantowego.")
    
# e) Znajdź sumę wszystkich macierzy gęstości P ρλ
sum_density_matrices = np.sum(density_matrices, axis=0)
print("\nSuma wszystkich macierzy gęstości P ρλ:")
print(sum_density_matrices)