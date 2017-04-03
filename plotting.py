from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X = np.arange(-100, 100, 0.25)
Y = np.arange(-100, 100, 0.25)
X, Y = np.meshgrid(X, Y)
Z = X**3*Y**3-3*X*Y**3-3*X**3*Y+9*X*Y
# Z = X**3 + Y **3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)

plt.show()


