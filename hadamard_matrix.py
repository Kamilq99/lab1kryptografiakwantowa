# Definicja macierzy operatora Hadamarda
Hadamard_matrix = np.array([[1, 1],
                             [1, -1]]) / np.sqrt(2)

print("\nMacierz operatora Hadamarda:")
print(Hadamard_matrix)

# a) Jakie wektory otrzymamy jeśli na wejście podamy odpowiednio stany 0 oraz 1?
print("\na) Wektory po zastosowaniu operatora Hadamarda:")
state_0 = np.array([1, 0])
state_1 = np.array([0, 1])
print("Stan 0:", np.dot(Hadamard_matrix, state_0))
print("Stan 1:", np.dot(Hadamard_matrix, state_1))

# b) Utwórz prosty obwód kwantowy z bramką Hadamarda na jednym rejestrze i bramką identyczności na drugim
qc = QuantumCircuit(2)
qc.h(0)  # Bramka Hadamarda na pierwszym rejestrze
qc.i(1)  # Bramka identyczności na drugim rejestrze

print("\nObwód kwantowy:")
print(qc.draw())

# c) Podać na wejście wybraną kombinację stanów 0 i 1 i zinterpretować wyniki
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
output_state = result.get_statevector(qc)

print("\nWynik po zastosowaniu obwodu kwantowego:")
print(output_state)

## Uruchamianie

Aby uruchomić skrypty, użyj następujących poleceń:

```bash
python matrix.py
python hadamard_matrix.py