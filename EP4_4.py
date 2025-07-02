from typing import Protocol

class Desenhavel(Protocol):
  def desenhar(self) -> str: ...

class Circulo(Desenhavel):
  def desenhar(self) -> str: 
    return f"Desenhando um Círculo com *"

class Quadrado(Desenhavel):
  def desenhar(self) -> str: 
    return f"Desenhando um Quadrado com *"

FORMA = {
  "Circulo": Circulo,
  "Quadrado": Quadrado
}

forma = input()
forma = FORMA[forma]()
print(forma.desenhar())