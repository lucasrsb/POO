from typing import Protocol

class Transporte(Protocol):
  def mover(self) -> str: ...

class Carro(Transporte):
  def mover(self) -> str:
    return f"Dirigindo o carro..."

class Bicicleta(Transporte):
  def mover(self) -> str:
    return f"Pedalando a bicicleta..."

class Trem(Transporte):
  def mover(self) -> str:
    return f"O trem está em movimento nos trilhos..."

TRANSPORTE = {
  "Carro": Carro,
  "Bicicleta": Bicicleta,
  "Trem": Trem,
}

transporte=input()
transporte=TRANSPORTE[transporte]()
print(transporte.mover())
