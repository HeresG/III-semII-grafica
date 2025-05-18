# trasati un sistem de axe de const in python

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# axa Ox
ax.axhline(0, color='black', linewidth=1)
# axa Oy
ax.axvline(0, color='black', linewidth=1)

ax.annotate('', xy=(10, 0), xytext=(0, 0),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))
ax.annotate('', xy=(0, 10), xytext=(0, 0),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))

ax.text(10.2, 0.2, 'X', fontsize=12)
ax.text(0.2, 10.2, 'Y', fontsize=12)
ax.text(-0.5, -0.5, 'O', fontsize=12)

# aspect pătrat
ax.grid(True, which='both')
ax.set_aspect('equal', 'box')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.title("Sistem de axe 2D")
plt.show()
