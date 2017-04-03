import sympy as S
import numpy as np
#Define variables and functions
x = S.symbols('x')
y = S.symbols('y')
f = x**3*y**3-3*x*y**3-3*x**3*y+9*x*y
#Differentiate f
fx = S.diff(f, x)
fy = S.diff(f, y)
#Find ciritcal points
X=S.solve([fx, fy],(x,y))
#Find Hessian of f
Hf = S.hessian(f,(x,y))
#Print critical point with corresponding hessian
for x0 in X:
    # S.pprint(x0)
    # S.pprint(Hf.subs({x: x0[0], y: x0[1]}))
    H=Hf.subs({x: x0[0], y: x0[1]})
    HM=H.eigenvals()
    print('Eigenvalues at {} are {}:'.format(x0, HM))
    # S.pprint(HM)







