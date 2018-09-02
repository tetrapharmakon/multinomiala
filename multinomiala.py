import itertools

class Monomial:
  def __init__(self,coef,vees,exps):
    self.coef = coef
    self.vees = vees
    self.exps = exps

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

  def _reduce(self,ls): 
    return [(key, sum(i[1] for i in group)) for key, group in itertools.groupby(sorted(ls, key = lambda i: i[0]), lambda i: i[0])]
  
  def __len__(self):
    return len(self.vees)

  def __lt__(self,other):
    if sum(self.exps) != sum(other.exps):
      return sum(self.exps) < sum(other.exps)
    else:
      return self.exps < other.exps

  def __mul__(self,other):
    l1, l2 = zip(*self.__reduce(zip(self.vees + other.vees, self.exps + other.exps)))
    return Monomial(self.coef * other.coef, list(l1), list(l2))
  
  def __pow__(self, n):
    f = lambda s,n:map(lambda x:x*n,s)
    return Monomial(self.coef ** n, self.vees, f(self.exps,n))

  def __eq__(self,other):
    if self.coef == other.coef and self.coef == 0:
      return True
    else:
      return all([self.coef == other.coef, sorted(zip(self.vees,self.exps)) == sorted(zip(other.vees,other.exps))])


class Polynomial:
# a Polynomial is a list of monomials
  def __init__(self, P):
    self.P = P

  def show(self):
    return ' + '.join(map(lambda x:x.show(), self.P))

  def __mul__(self,other):
    return [i * j for i in self.P for j in other.P]