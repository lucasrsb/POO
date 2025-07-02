class Pessoa():
  def __init__(self, nome, filhos=None):
    self.nome = nome
    self.filhos = []

  def adicionar_filho(self, filho):
    self.filhos.append(filho)

  def contar_filhos(self):
    total=len(self.filhos)
    for filho in self.filhos:
      total+=filho.contar_filhos()
    return total

class Pai():
  pass

class Filho():
  pass

total=int(input())
pessoas={}

for _ in range(total):
  nome_pai, no_filhos = input().split()
  if nome_pai not in pessoas:
    pessoas[nome_pai] = Pessoa(nome_pai)

  for _ in range(int(no_filhos)):
    nome_filho = input()
    if nome_filho not in pessoas:
      pessoas[nome_filho] = Pessoa(nome_filho)
    pessoas[nome_pai].adicionar_filho(pessoas[nome_filho])

    
pessoa=input()
print(pessoas[pessoa].contar_filhos())
