import sympy
from sympy import symbols
from sympy.solvers import solve 

x = symbols('x')

# Put the equation here:

eq = 5*(2*x - 1)>=3*x+7+x

print("x =", str(solve(eq,x)))