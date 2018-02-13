import sympy as sym
import math

#print(math.sqrt(8))
#print(sym.sqrt(8))

#numerator, denominator
#r1 = sym.Rational(4, 5)
#r2 = sym.Rational(5, 4)

#print("r1 ", r1, " r2 ", r2, " addition ",r1+r2, " multiplication ", r1*r2,
#      " division ",r1/r2)

#print(sym.sqrt(r1))

#x, y = sym.symbols("x y")
#exp1 = y + 2 * x
#exp2 = 2 * x + sym.sqrt(y)

#print(exp1, "|", exp2)

#print(exp1 + x * 100)

#y*(2*x+y) -- will leave in factored form
#print(exp1 * y)

#2*x**2 + x*y -- distributes the x into the 2x+y
#print(sym.expand(x * (2 * x + y)))

#x*(2*x + y) -- factors out the extra x
#print(sym.factor(2*x**2+x*y))

#Can choose to have sympy print to ascii, unicode, latex, etc
#works better with ipython notebooks

#.doit will execute an integral. Can also use sym.Integrate

#x, a, b, y = sym.symbols("x a b y")
#print(sym.Integral(x**3, (x, a, b)).doit())

#can also do y, 3 instead of yyy
#print(sym.Derivative(y**3, y, 2).doit())

#############################################
#solve for x

x, y, z = sym.symbols("x y z")

#x^2 - x = 0. comma replaces equals here
#equation = sym.Eq(x**2 -x, 0)
#print(sym.solve(equation))

#factorized
#equation = sym.Eq(x**2 - 4, x)
#print(sym.factor(equation))

#simplify
#equation = sym.Eq((x-2)*(x+2))
#print(sym.simplify(equation))

#factorization will cancel similar factors
#print(sym.factor((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))

#(1, [(x - 1, 1), (x + 1, 2)])
# x-1, 1 means x-1 appears once
# 1, the rest means the rest appeared once. Repeated would have been 2,
#print(sym.factor_list(x**3 + x**2 - x -1))

#partial fractions
#fraction = (4*x**3 + 21*x**2 + 10*x + 12) / (x**4 + 5*x**3 + 5*x**2 + 4*x)
#fraction = sym.apart(fraction)
#print(fraction)
#fraction = sym.simplify(fraction)
#print(fraction)

#A = sym.Matrix([[1.0, 2.0], [-(1.0/2.0), 1.0]])
#B = sym.Matrix([[5.0, 7.0], [(1.0/2.0), 11.0]])
#print(A*B)

#print(A.inv())