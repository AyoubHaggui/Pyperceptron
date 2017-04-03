import sympy as S

x = S.symbols('x')
y = S.symbols('y')
f= x**3*y**3-3*x*y**3-3*x**3*y+9*x*y
fx = S.diff(f, x)
fy = S.diff(f, y)
fxy = S.diff(f,x,y)
S.init_printing()
S.pprint(f)
S.pprint(fx)
S.pprint(fy)
S.pprint(fxy)
a=S.solve([fx, fy],[x,y])
print("critical points: ")
S.pprint(a)
