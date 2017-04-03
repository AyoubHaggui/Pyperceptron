import sympy as S

x = S.symbols('x')
y = S.symbols('y')
f= x**3*y**3-3*x*y**3-3*x**3*y+9*x*y
#Calculating Hessian
Hf = S.hessian(f, (x,y))
S.pprint(Hf)