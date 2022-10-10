"""
from sympy import symbols, diff

a, b = symbols("x, y")
print(f"Cost func(x,y) : {f(a, b)}")

print(f"Partial derivative: { diff(f(a, b), a) }") # Partial derivative regarding to a (x)
print(f"Value of f(x,y) with x=1.8 y=1.0 is : { f(a, b).evalf(subs={a:1.8, b:1.0}) }") # Cost
"""