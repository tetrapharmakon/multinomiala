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
  pass

def test_pow():
  pass

def test_add():
  pass

def test_mul():
  pass

def test_len():
  pass

def test_eq():
  pass

def test_show_list():
  assert Polynomial([a]).show_list() == ['3']
  assert Polynomial([b]).show_list() == ['x']
  assert Polynomial([a]) * Polynomial([b]) == Polynomial([a * b])
  assert Polynomial([b]) * Polynomial([c]) == Polynomial([b * c])
  assert Polynomial([e]) * Polynomial([f]) == Polynomial([e * f])

def test_show():
  assert Polynomial([a,b,c]).show() == '3 + x + y'
  assert Polynomial([g,f,u]).show() == '3y + 2x + 3x^2y^3'
  assert Polynomial([u**2,d,u]).show() == '9x^4y^6 + x^3 + 3x^2y^3'
  assert (Polynomial([a]) * Polynomial([b])).show() == '3x'
