def aitken_interpolation(x_values, y_values, x):
    """
    Implementarea metodei Aitken pentru interpolare.

    x_values: lista valorilor x_i
    y_values: lista valorilor f(x_i)
    x: valoarea la care se evaluează interpolarea

    Returnează: P(x) - valoarea aproximată în punctul x
    """
    n = len(x_values)

    # Inițializăm tabelul Aitken cu 0
    P = [[0.0 for _ in range(n)] for _ in range(n)]

    # Coloana inițială: f(x_i)
    for i in range(n):
        P[i][0] = y_values[i]

    # Construim tabelul Aitken
    for j in range(1, n):
        for i in range(n - j):
            xi = x_values[i]
            xj = x_values[i + j]
            Pi_j_1 = P[i][j - 1]
            Pi1_j_1 = P[i + 1][j - 1]

            # Formula Aitken
            P[i][j] = ((x - xj) * Pi_j_1 + (xi - x) * Pi1_j_1) / (xi - xj)

    return P[0][n - 1]


# Exemplu
if __name__ == "__main__":
    x_vals = [1.0, 1.3, 1.6, 1.9, 2.2]
    y_vals = [0.7652, 0.6201, 0.4554, 0.2818, 0.1103]

    # Punctul în care evaluăm
    x_eval = 1.5

    # Apelul funcției
    rezultat = aitken_interpolation(x_vals, y_vals, x_eval)

    print(f"Valoarea aproximată a funcției în x = {x_eval} este {rezultat:.6f}")
