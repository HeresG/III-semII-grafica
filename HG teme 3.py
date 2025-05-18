#Generati un sistem de axe ortogonale OXY in Python, In acest sistem de axe sa se traseze 3
#drepte, una verƟcala, una orizontala, una oblica, si de culori diferite.


import matplotlib.pyplot as plt

# Setam figura și axele
fig, ax = plt.subplots()

# Desenam axele OX și OY
ax.axhline(y=0, color='black', linewidth=1)  # axa OX
ax.axvline(x=0, color='black', linewidth=1)  # axa OY

# Dreaptă verticală (ex: x = 2)
x_vert = [2, 2]
y_vert = [-10, 10]
ax.plot(x_vert, y_vert, color='red', label='verticală x=2')

# Dreaptă orizontală (ex: y = 3)
x_horiz = [-10, 10]
y_horiz = [3, 3]
ax.plot(x_horiz, y_horiz, color='blue', label='orizontală y=3')

# Dreaptă oblică (ex: y = 0.5x + 1)
x_oblic = [-10, 10]
y_oblic = [0.5 * x + 1 for x in x_oblic]
ax.plot(x_oblic, y_oblic, color='green', label='oblică y=0.5x+1')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True, linestyle='--', linewidth=0.5)
ax.set_aspect('equal')

ax.legend()

plt.title("Sistem de axe OXY și 3 drepte")

# Afișare grafic
plt.show()
