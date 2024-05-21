# Lista zadań z QCrypt 1

## Wprowadzenie

Ten projekt zawiera rozwiązania zadań z QCrypt 1, dotyczących analizy operatora kwantowego oraz podstawowych operacji na stanach kwantowych przy użyciu biblioteki Qiskit.

## Wymagania

Aby uruchomić skrypty zawarte w repozytorium, należy zainstalować następujące biblioteki:
- Qiskit
- numpy

Można je zainstalować za pomocą poniższego polecenia:
```bash
pip install qiskit numpy

# Zadania

## Zadanie 1: Instalacja bibliotek

Jeśli potrzeba, zainstalować bibliotekę Qiskit i numpy (lub inną wybraną).

## Zadanie 2: Rozwiązywanie zagadnienia własnego operatora

1. Wprowadzić macierz operatora \( \hat{M} \):
   \[
   \hat{M} =
   \begin{bmatrix}
   1 & -1 + i & 1 & -1 - i \\
   -1 + i & 1 & -1 - i & 1 \\
   1 & -1 - i & 1 & -1 + i \\
   -1 - i & 1 & -1 + i & 1
   \end{bmatrix}
   \]

2. Znaleźć wartości własne \( \lambda \) macierzy \( \hat{M} \).

3. Znaleźć odpowiadające im wektory własne \( \psi\_\lambda \).

4. Skonstruować odpowiadające im macierze gęstości \( \rho\_\lambda \).

## Zadanie 3: Własności rozwiązań

1. Sprawdzić, czy \( \rho \) jest samosprzężona.

2. Sprawdzić, czy \( \rho \) są dodatnio określone.

3. Sprawdzić idempotyczność \( \rho^2 = \rho \).

4. Sprawdzić, ile wynoszą ślady \( \text{Tr}(\rho) \) oraz \( \text{Tr}(\rho^2) \). Co to oznacza?

5. Znaleźć sumę wszystkich macierzy gęstości \( \sum \rho\_\lambda \).

## Zadanie 4: Operator Hadamarda

1. Wprowadzić macierz operatora Hadamarda \( \hat{H} \).

2. Jakie wektory otrzymamy, jeśli na wejście podamy odpowiednio stany \( |0\rangle \) oraz \( |1\rangle \)?

3. Utworzyć prosty obwód kwantowy, w którym na jeden z rejestrów będziemy działać bramką \( \hat{H} \), a na drugi \( \hat{I} \).

4. Podać na wejście wybraną kombinację stanów \( |0\rangle \) i \( |1\rangle \) i zinterpretować wyniki.

