# deduceti ecuatiile rotatiei in jurul originii
# x'= x cos O - y sin O
# y'= x sin O + y cos O , O= unghi de rotatie
# (x,y) -> (x',y')

import matplotlib.pyplot as plt
import numpy as np
import math

# Funcția de rotație
def roteste_punct(x, y, theta):
    rad = math.radians(theta)
    x_rot = x * math.cos(rad) - y * math.sin(rad)
    y_rot = x * math.sin(rad) + y * math.cos(rad)
    return x_rot, y_rot

# Coordonatele triunghiului original
A = (1, 1)
B = (4, 1)
C = (2.5, 4)

# se rotesc toate punctele cu 45 de grade
theta = 45
A_rot = roteste_punct(*A, theta)
B_rot = roteste_punct(*B, theta)
C_rot = roteste_punct(*C, theta)

triunghi_original = np.array([A, B, C, A])
triunghi_rotit = np.array([A_rot, B_rot, C_rot, A_rot])

plt.figure(figsize=(6, 6))
plt.plot(triunghi_original[:, 0], triunghi_original[:, 1], 'b-', label='Original')
plt.plot(triunghi_rotit[:, 0], triunghi_rotit[:, 1], 'r--', label='Rotit 45°')

# Axele
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('Rotație triunghi în jurul originii')
plt.grid(True)
plt.show()
