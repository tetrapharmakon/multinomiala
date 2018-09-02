from multinomiala import *

def test_show():
  assert Monomial(0, [], []).show() == '0'
  assert Monomial(0, ["x"], [1]).show() == '0'
  assert Monomial(1, ["x"], [1]).show() == 'x'
  assert Monomial(1, ["x", "y"], [1,1]).show() == 'xy'
  assert Monomial(3, ["x", "y"], [1,1]).show() == '3xy'
  assert Monomial(1, ["x"], [4]).show() == 'x^4'
  assert Monomial(2, ["x"], [3]).show() == '2x^3'
  assert Monomial(5, ["x", "y"], [3,4]).show() == '5x^3y^4'
  assert Monomial(4, ["x", "y", "z", "t"], [4,3,2,1]).show() == '4tx^4y^3z^2'
  assert Monomial(2, ['y', 'x'], [2, 1]).show() == '2xy^2'
  assert Monomial(6, ["x"], [0]).show() == '6'
  assert Monomial(6, [""], [0]).show() == '6'
  assert Monomial(1, ["x"], [0]).show() == '1'
  assert Monomial(2, ["y"], [0]).show() == '2'
  assert Monomial(3, ['x','y','y','z'], [2,3,2,3]).show() == '3x^2y^5z^3'
  assert Monomial(3, ['a','b','b','a', 'c','c','c','d','e'], [2,3,2,3,4,3,6,1,2]).show() == '3a^5b^5c^13de^2'
  assert Polynomial([a,b,c]).show() == '3 + x + y'
  assert Polynomial([g,f,u]).show() == '3y + 2x + 3x^2y^3'
  assert Polynomial([u**2,d,u]).show() == '9x^4y^6 + x^3 + 3x^2y^3'
  assert (Polynomial([a]) * Polynomial([b])).show() == '3x'
  ############

a = Monomial(3,[''], [0])
b = Monomial(1, ['x'], [1])
c = Monomial(1, ['y'], [1])
d = Monomial(1, ['x'], [3])
e = Monomial(1, ['y'], [4])
f = Monomial(2, ['x'], [1])
g = Monomial(3, ['y'], [1])

u = Monomial(3,['x','y'],[2,3])
v = Monomial(6, ['x','z'], [3,3])

def test_multiply():
  assert (a * a).show() == '9'
  assert (a * b).show() == '3x'
  assert (b * c).show() == 'xy'
  assert (c * d).show() == 'x^3y'
  assert (d * c).show() == 'x^3y'
  assert (g * b).show() == '3xy'
  assert (u * v).show() == '18x^5y^3z^3'

def test_len():
  assert len(v) == 2
  assert len(Monomial(3, ['a','b','c'], [1,1,1])) == 3
  assert len(Monomial(3, [''], [0])) == 1

def test_eq():
  assert Monomial(0,[],[]) == Monomial(0,[],[])
  assert Monomial(0,[],[]) == Monomial(0,['a'],[1])
  assert Monomial(0,[],[]) == Monomial(0,['a'],[2])
  assert Monomial(2,['x'],[1]) == Monomial(2,['x'],[1])
  assert (u ** 3) == Monomial(27, ['x','y'],[6,9])
  assert (u * v).coef == 18
  assert (u * v).vees == ['x','y','z']
  assert (u * v).exps == [5,3,3]
  assert (u * v)**2 == Monomial(324,['x','y','z'], [10,6,6])