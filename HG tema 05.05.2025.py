
#rotirea celor doua axe

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def rotate(x, y, angle, cx=0, cy=0):
    s, c = np.sin(angle), np.cos(angle)
    x, y = x - cx, y - cy
    x_new = x * c - y * s + cx
    y_new = x * s + y * c + cy
    return x_new, y_new

def draw_triangle(ax, tip, direction, size=0.4):
    dx, dy = direction
    length = np.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    px, py = -uy, ux

    # Baza triunghiului
    base_center = (tip[0] - ux * size, tip[1] - uy * size)
    left = (base_center[0] + px * size / 2, base_center[1] + py * size / 2)
    right = (base_center[0] - px * size / 2, base_center[1] - py * size / 2)

    triangle = np.array([tip, left, right, tip])
    ax.plot(triangle[:, 0], triangle[:, 1], 'k')

def update(frame):
    ax.clear()

    # dreptunghi fix
    rect = np.array([
        [-0.5, -1.2],
        [0.5, -1.2],
        [0.5, 1.2],
        [-0.5, 1.2],
        [-0.5, -1.2]
    ])
    ax.plot(*zip(*rect), 'b')

    # punct central
    ax.plot(0, 0.5, 'ko', markersize=6)

    # axe
    horiz = [(-1.5, 0.5), (1.5, 0.5)]
    vert = [(0, -2), (0, 2)]

    # rotire axă
    angle = np.radians(frame)
    horiz_rot = [rotate(x, y, angle, 0, 0.5) for (x, y) in horiz]
    vert_rot = [rotate(x, y, angle, 0, 0.5) for (x, y) in vert]

    # axele
    ax.plot(*zip(*horiz_rot), 'k', linewidth=2)
    ax.plot(*zip(*vert_rot), 'k', linewidth=2)

    # triunghiuri în capete
    draw_triangle(ax, horiz_rot[0], direction=np.subtract([0, 0.5], horiz_rot[0]))
    draw_triangle(ax, horiz_rot[1], direction=np.subtract([0, 0.5], horiz_rot[1]))
    draw_triangle(ax, vert_rot[0], direction=np.subtract([0, 0.5], vert_rot[0]))
    draw_triangle(ax, vert_rot[1], direction=np.subtract([0, 0.5], vert_rot[1]))

    ax.set_aspect('equal')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.axis('off')
    ax.set_title("Rotirea celor două axe")

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
plt.show()
