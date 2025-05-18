import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rotatie_z(puncte, unghi_degrees):
    #Aplică o rotație în jurul axei Z unui set de puncte 3D.
    theta = np.radians(unghi_degrees)
    matrice_rotatie = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])
    return np.dot(puncte, matrice_rotatie.T)

# Punctele unui pătrat în planul XY
patrat = np.array([
    [1, 1, 0],
    [1, -1, 0],
    [-1, -1, 0],
    [-1, 1, 0],
    [1, 1, 0]
])

# Aplicăm rotație cu 45 de grade în jurul axei Z
patrat_rotit = rotatie_z(patrat, 45)

# Afișare grafică
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Pătratul inițial - albastru
ax.plot(patrat[:, 0], patrat[:, 1], patrat[:, 2], label="Inițial", color='blue')

# Pătratul rotit - roșu
ax.plot(patrat_rotit[:, 0], patrat_rotit[:, 1], patrat_rotit[:, 2], label="Rotit", color='red')

# Axele 3D
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Rotire în jurul axei Z")
ax.legend()
plt.show()
