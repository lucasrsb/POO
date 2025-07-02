class Calculadora():
  def somar(self, *args):
    if len(args) == 0:
      return "" 
    if isinstance(args[0],str):
      return "".join(args)
    return sum(args) 

calc = Calculadora()
tipo = input()
lista = []
for _ in range(int(tipo[-1])):
  lista.append({"int": int, "float": float, "str": str}[tipo[:-1]](input()))
print(calc.somar(*lista))

