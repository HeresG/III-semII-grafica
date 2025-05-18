#algoritmul de rasterizare al lui Bresenham

import matplotlib.pyplot as plt

def bresenham(x0, y0, x1, y1):
#Algoritmul lui Bresenham pentru trasarea unei linii între (x0, y0) și (x1, y1).
    puncte = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        puncte.append((x0, y0))  #pixelul curent
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            err = err + dx
            y0 = y0 + sy
    return puncte

# Exemplu: linie de la (2, 3) la (15, 8)
linie = bresenham(2, 3, 15, 8)

# Afișăm grafic
x_vals, y_vals = zip(*linie)
plt.figure(figsize=(6, 6))
plt.scatter(x_vals, y_vals, c='black', marker='s')
plt.grid(True)
plt.xticks(range(0, max(x_vals)+2))
plt.yticks(range(0, max(y_vals)+2))
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Algoritmul lui Bresenham - Linie discretizată")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
