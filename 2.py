import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Sample data - generating a 3D surface
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Create the plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(10, 7))
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the plot
ax.set_title("Wykres 3D: Fala sinusoidalna")
ax.set_xlabel("Oś X")
ax.set_ylabel("Oś Y")
ax.set_zlabel("Oś Z")

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()
