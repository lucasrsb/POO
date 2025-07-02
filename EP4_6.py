from typing import Protocol

class MetodoPagamento(Protocol):
  def pagar(self, valor: float) -> str: ...

class CartaoCredito(MetodoPagamento):
  def pagar(self, valor: float) -> str: 
    return f"Pagando R${valor:.1f} com Cartão de Crédito"
  
class Boleto(MetodoPagamento):
  def pagar(self, valor: float) -> str: 
    return f"Pagando R${valor:.1f} via Boleto"

class Pix(MetodoPagamento):
  def pagar(self, valor: float) -> str: 
    return f"Pagando R${valor:.1f} via Pix"
  
METODO = {
  "Cartao": CartaoCredito,
  "Boleto": Boleto,
  "Pix": Pix,
}

metodo = input()
valor=float(input())
metodo = METODO[metodo]()
print(metodo.pagar(valor))