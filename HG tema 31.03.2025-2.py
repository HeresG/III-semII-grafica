#implementati algoritmul DDA

import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    points = []

    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

# Exemplu: avem o linie de la (2, 3) la (15, 10)
linie = dda(2, 3, 15, 10)

x_vals, y_vals = zip(*linie)

plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='s', color='blue', linestyle='None')
plt.grid(True)
plt.xticks(range(0, 20))
plt.yticks(range(0, 20))
plt.gca().invert_yaxis()
plt.title("Algoritmul DDA - Linie de la (2,3) la (15,10)")
plt.show()
