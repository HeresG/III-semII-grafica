#implementati algoritmul lui bresenham

import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    points.append((x2, y2))
    return points


# Exemplu: avem o linie de la (2, 3) la (15, 10)
linie = bresenham(2, 3, 15, 10)

x_vals, y_vals = zip(*linie)

plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='s', color='black', linestyle='None')
plt.grid(True)
plt.xticks(range(0, 20))
plt.yticks(range(0, 20))
plt.gca().invert_yaxis()
plt.title("Algoritmul lui Bresenham - Linie de la (2,3) la (15,10)")
plt.show()
