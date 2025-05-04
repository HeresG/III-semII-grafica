# transformati prin oglindire si implem oglindirea pentru A(1,2,3) , B(-1,-2,-3)

import numpy as np
import matplotlib.pyplot as plt

# Punctele date
A = np.array([1, 2, 3])
B = np.array([-1, -2, -3])

# oglindire
def oglindire_YZ(p):  # inversăm X
    return np.array([-p[0], p[1], p[2]])

def oglindire_XZ(p):  # inversăm Y
    return np.array([p[0], -p[1], p[2]])

def oglindire_XY(p):  # inversăm Z
    return np.array([p[0], p[1], -p[2]])

# noile puncte
A_yz = oglindire_YZ(A)
B_yz = oglindire_YZ(B)

A_xz = oglindire_XZ(A)
B_xz = oglindire_XZ(B)

A_xy = oglindire_XY(A)
B_xy = oglindire_XY(B)

# 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Functie desenat puncte
def plot_punct(p, label, color):
    ax.scatter(p[0], p[1], p[2], color=color)
    ax.text(p[0], p[1], p[2], f'{label}', fontsize=9)

# Puncte originale
plot_punct(A, 'A', 'blue')
plot_punct(B, 'B', 'blue')

# Oglindiri
plot_punct(A_yz, "A'", 'red')
plot_punct(B_yz, "B'", 'red')

plot_punct(A_xz, "A''", 'green')
plot_punct(B_xz, "B''", 'green')

plot_punct(A_xy, "A'''", 'purple')
plot_punct(B_xy, "B'''", 'purple')

# Setări axă
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Oglindirea punctelor în 3D")

plt.show()
