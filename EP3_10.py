class Calculadora():
  def somar(self, a, b=None, c=None):
    if c is None:
      if b is None:
        return a
      return a + b
    return a + b + c

calc = Calculadora()

