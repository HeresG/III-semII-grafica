import math

# Punctul A
x, y = 2, 4

# Unghiul de rotație (30° în radiani)
theta_deg = 30
theta_rad = math.radians(theta_deg)

# Formula rotației în jurul originii:
x_rot = x * math.cos(theta_rad) - y * math.sin(theta_rad)
y_rot = x * math.sin(theta_rad) + y * math.cos(theta_rad)

print(f"Coordonatele punctului A după rotație de 30°: x = {x_rot:.2f}, y = {y_rot:.2f}")
