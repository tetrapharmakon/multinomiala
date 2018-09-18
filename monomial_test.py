from multinomiala import *

a = Monomial(3, {' ': 0})
b = Monomial(1, {'x': 1})
c = Monomial(1, {'y': 1})
d = Monomial(1, {'x': 3})
e = Monomial(1, {'y': 4})
f = Monomial(2, {'x': 1})
g = Monomial(3, {'y': 1})

u = Monomial(3, {'x': 2, 'y': 3})
v = Monomial(6, {'x': 3, 'z': 3})

z = Monomial(0, {})

def test_init():
  assert Monomial(1, {'x': 1, 'x': 1}).vees == ['x']
  assert Monomial(1, {'x': 1, 'x': 3}).exps == [3]
  assert Monomial(1, {'x': 0}).vees == []
  assert Monomial(1, {'x': 0}).exps == []
  assert Monomial(0, {'x': 1}).vees == []
  assert Monomial(0, {'x': 1}).exps == []

def test_pow():
  assert a ** 3 == Monomial(27,{})
  assert b ** 3 == Monomial(1, {'x': 3})
  assert c ** 2 == Monomial(1, {'y': 2})
  assert (d * e)**2 == Monomial(1, {'x': 6, 'y': 8}) # (x^3y^4)^2
  assert z**4 == Monomial(0, {})

def test_add():
  pass

def test_mul():
  assert a * a == Monomial(9, {'x': 0}) #'9'
  assert a * b == Monomial(3, {'x': 1}) #'3x'
  assert b * c == Monomial(1, {'x': 1, 'y': 1}) #'xy'
  assert c * d == Monomial(1, {'x': 3, 'y': 1}) # 'x^3y'
  assert d * c == Monomial(1, {'x': 3, 'y': 1}) # 'x^3y'
  assert g * b == Monomial(3, {'x': 1, 'y': 1}) # '3xy'
  assert u * v == Monomial(18, {'y': 3, 'x': 5, 'z': 3}) #'18x^5y^3z^3'

def test_len():
  assert len(v) == 2
  assert len(Monomial(3, {'a': 1, 'c': 1, 'b': 1})) == 3
  assert len(Monomial(3, {'x': 0})) == 0

def test_eq():
  assert Monomial(0, {}) == Monomial(0, {'a': 0})
  assert Monomial(0, {}) == Monomial(0, {'a': 1})
  assert Monomial(0, {}) == Monomial(0, {'a': 2})
  assert (u ** 3) == Monomial(27, {'x': 6, 'y': 9})
  assert (u * v) == Monomial(18, {'x': 5, 'y': 3, 'z': 3})

def test_show():
  assert Monomial(0, {}).show() == '0'
  assert Monomial(0, {"x": 1}).show() == '0'
  assert Monomial(1, {"x": 1}).show() == 'x'
  assert Monomial(1, {"x": 1, "y":1}).show() == 'xy'
  assert Monomial(3, {"x": 1, "y": 1}).show() == '3xy'
  assert Monomial(1, {"x": 4}).show() == 'x^4'
  assert Monomial(2, {"x": 3}).show() == '2x^3'
  assert Monomial(5, {"x": 3, "y":4}).show() == '5x^3y^4'
  assert Monomial(4, {'y': 3, 'x': 4, 'z': 2, 't': 1}).show() == '4tx^4y^3z^2'
  assert Monomial(2, {'y': 2, 'x':1}).show() == '2xy^2'
  assert Monomial(6, {"x": 0}).show() == '6'
  assert Monomial(6, {"a": 0}).show() == '6'
  assert Monomial(1, {"x": 0}).show() == '1'
  assert Monomial(2, {"y": 0}).show() == '2'
  assert Monomial(3, {'x':2, 'y':5, 'z':3}).show() == '3x^2y^5z^3'
  