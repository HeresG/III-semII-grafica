import math

# Coordonatele carteziene
x, y = 3, 4

# Conversie în coordonate polare
r = math.sqrt(x**2 + y**2)
theta_rad = math.atan2(y, x)  # unghiul în radiani
theta_deg = math.degrees(theta_rad)  # conversie în grade

print(f"Coordonate polare: r = {r:.2f}, θ = {theta_deg:.2f}°")

# Conversie inversă în coordonate carteziene
x2 = r * math.cos(theta_rad)
y2 = r * math.sin(theta_rad)

print(f"Coordonate carteziene din polare: x = {x2:.2f}, y = {y2:.2f}")
