"""
3D Charts

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm # color map

Make the data
x = np.linspace(start=-2, stop=2, num=200)
y = np.linspace(start=-2, stop=2, num=200)
print(f"Shape of X array {x.shape}") # Vector

Coordinate vector to coordinate matrix
x, y = np.meshgrid(x, y)

Generating 3D Plot (x, y, z)
fig = plt.figure(figsize=[16, 12]) # Generating an instance
axes = fig.gca(projection="3d") # Get current axes
axes.set_xlabel("X", fontsize=20)
axes.set_ylabel("Y", fontsize=20)
axes.set_zlabel("f(x,y) - Cost", fontsize=20)

Plot with color pallet
axes.plot_surface(x, y, f(x, y), cmap=cm.coolwarm, alpha=0.8)


plt.show()
"""