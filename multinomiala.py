import itertools

class Monomial:
  def __init__(self,coef,vees_exps):
    self.coef = coef
    if self.coef == 0:
      self.vees = []
      self.exps = []
    else:
      vees_exps = dict(filter(lambda (_,y): y != 0, vees_exps.items()))
      self.vees = vees_exps.keys()
      self.exps = vees_exps.values()

  def _reduce(self,ls): 
    return [(key, sum(i[1] for i in group)) for key, group in itertools.groupby(sorted(ls, key = lambda i: i[0]), lambda i: i[0])]
  
  def __len__(self):
    return len(self.vees)

  def __mul__(self,other):
    reduced = self._reduce(zip(self.vees + other.vees, self.exps + other.exps))
    if reduced == []:
      l1, l2 = [], []
    else:
      l1, l2 = zip(*reduced)
    return Monomial(self.coef * other.coef, dict(zip(list(l1), list(l2))))
  
  def __pow__(self, n):
    f = lambda s,n:map(lambda x:x*n,s)
    return Monomial(self.coef ** n, dict(zip(self.vees, f(self.exps,n))))

  def __eq__(self,other):
    if self.coef == other.coef and self.coef == 0:
      return True
    else:
      return all([self.coef == other.coef, sorted(zip(self.vees,self.exps)) == sorted(zip(other.vees,other.exps))])

  def __add__(self,other):
    if self.vees == other.vees and self.exps == other.exps:
      return Monomial(self.coef + other.coef, self.vees,self.exps)
    else:
      return Polynomial([self,other])

  def show(self):
    el = self._elevate()
    if self.coef == 0:
      return '0'
    elif self.coef == 1:
      return '1' if el == '' else el
    else:
      return str(self.coef) + el
  
  def _caret(self,x,y):
    if y == 1:
      return x
    elif y == 0:
      return ''
    else: 
      return x + '^' + str(y)

  def _elevate(self):
    f = lambda (x,y):self._caret(x,y)
    straighten = sorted(zip(self.vees,self.exps))
    return ''.join(map(f,self._reduce(straighten)))



























class Polynomial:
# a Polynomial is a list of monomials
  def __init__(self, P):
    self.P = P

  def show_list(self):
    return map(lambda x:x.show(), self.P)

  def show(self):
    return ' + '.join(map(lambda x:x.show(), self.P))

  def __mul__(self,other):
    return Polynomial([i * j for i in self.P for j in other.P])

  def __eq__(self,other):
    return all([i == j for i in self.P for j in other.P])
