class CaixaMagica():
  def __init__(self,valor):
    self.valor = valor

  def processar(self, modo=None):
    if modo is None:
      return f"Presente: {self.valor}"
    self.valor+="!"
    if isinstance(valor,int):
      valor = f"Doces com {valor} calorias"
      return "; ".join([self.valor]*2)
    else:
      valor = f"Poção mágica com {valor} ml"
      return f"{self.valor} -> {modo}!"   

tipo = input()
valor = input()
modo = input()

if tipo == "int":
  valor = f"Doces com {valor} calorias"
elif tipo == "double":
  valor = f"Poção mágica com {valor} ml"

caixa = CaixaMagica(valor)
print(caixa.processar())
