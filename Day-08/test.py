import numpy as np

# Angle in degrees (example)
angle_degrees = 45

# Convert to radians
angle_radians = np.radians(angle_degrees)

# Magnitude or radius (optional, set to 1 for unit vector)
radius = 1

# Compute (x, y)
x = radius * np.cos(angle_radians)
y = radius * np.sin(angle_radians)

print(f"(x, y) for angle {angle_degrees}°: ({x}, {y})")
