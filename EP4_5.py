from typing import Protocol

class Conectavel(Protocol):
  def conectar(self) -> str: ...

  def desconectar(self) -> str: ...

class Bluetooth():
  def conectar(self) -> str:
    return f"Bluetooth conectado"

  def desconectar(self) -> str:
    return f"Bluetooth desconectado"

class WiFi():
  def conectar(self) -> str:
    return f"WiFi conectado"

  def desconectar(self) -> str:
    return f"WiFi desconectado"

TIPO = {
  "Bluetooth": Bluetooth,
  "WiFi": WiFi
}

tipo=input()
tipo=TIPO[tipo]()
print(tipo.conectar()) 
print(tipo.desconectar()) 
