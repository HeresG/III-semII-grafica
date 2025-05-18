#algoritmul lui Bresenham

import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1

    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

# exemplu: avem o linie de la (2, 3) la (15, 10)
linie = bresenham(2, 3, 15, 10)

x_vals, y_vals = zip(*linie)

plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='s', color='red', linestyle='None')
plt.grid(True)
plt.xticks(range(0, 20))
plt.yticks(range(0, 20))
plt.gca().invert_yaxis()
plt.title("Algoritmul lui Bresenham - Linie de la (2,3) la (15,10)")
plt.show()
