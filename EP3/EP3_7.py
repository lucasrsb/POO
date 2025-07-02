class Personagem():
  def __init__(self, nome, vida, dano):
    self.nome = nome
    self.vida = float(vida)
    self.dano = float(dano)

  def esta_morto(self):
    if self.vida <= 0:
      print(f"{self.nome} foi derrotado!\nBatalha encerrada!")
    return self.vida < 0

  def atacar(self, alvo):
    alvo.vida -= self.dano
    print(f"{self.nome} ataca {alvo.nome}! {alvo.nome} tem {alvo.vida:.1f} de vida.")
    return alvo.esta_morto()

class Guerreiro(Personagem):
  pass

class Mago(Personagem):
  def __init__(self, nome, vida, dano):
    super().__init__(nome, float(vida), float(dano)*1.5)
  

def simular_batalha(playerOne, playerTwo):
  while True:
    if playerOne.atacar(playerTwo) or playerTwo.atacar(playerOne): break

playerOne = input().split()
playerTwo = input().split()

CLASSES = {
  "G": Guerreiro,
  "M": Mago
}

playerOne = CLASSES[playerOne[0]](playerOne[1], playerOne[2], playerOne[3])
playerTwo = CLASSES[playerTwo[0]](playerTwo[1], playerTwo[2], playerTwo[3])

simular_batalha(playerOne, playerTwo)