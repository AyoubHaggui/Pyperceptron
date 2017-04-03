from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sympy as S


def fxy(x, y):
    return x**3*y**3-3*x*y**3-3*x**3*y+9*x*y

x = S.symbols('x')
y = S.symbols('y')
f= x**3*y**3-3*x*y**3-3*x**3*y+9*x*y
fx = S.diff(f, x)
fy = S.diff(f, y)
critical = S.solve([fx, fy],[x,y])
#Critical points 3d corrdinates
critical = np.array(critical)
for x, y in zip(critical[:,0], critical[:,1]):
    z = fxy(x, y)
#Plotting the function
X = np.arange(-100, 100, 0.25)
Y = np.arange(-100, 100, 0.25)
X, Y = np.meshgrid(X, Y)
Z = X**3*Y**3-3*X*Y**3-3*X**3*Y+9*X*Y
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
#plotting critical points
ax.scatter(critical[:,0], critical[:,1], z, c="red")


plt.show()


