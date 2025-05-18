#3d compunerea dintre o rotatie si o translatie

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# cub în 3D
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

faces = [
    [0,1,2,3],
    [4,5,6,7],
    [0,1,5,4],
    [2,3,7,6],
    [1,2,6,5],
    [0,3,7,4]
]

def rotatie_z(puncte, unghi_gr):
    theta = np.radians(unghi_gr)
    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])
    return np.dot(puncte, Rz.T)

# Funcție translație
def translatie(puncte, v):
    return puncte + v

#rotație apoi translație
unghi = 45
trans_vector = np.array([2, 1, 1])

rotated = rotatie_z(vertices, unghi)
rotated_translated = translatie(rotated, trans_vector)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def plot_cub(puncte, culoare, alpha=0.5):
    for face in faces:
        ax.add_collection3d(Poly3DCollection([puncte[face]], facecolors=culoare, linewidths=1, edgecolors='k', alpha=alpha))

plot_cub(vertices, 'lightblue')
plot_cub(rotated_translated, 'orange')

ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])
ax.set_title("Rototranslație în 3D")

plt.show()
