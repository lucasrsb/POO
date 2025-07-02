from abc import ABC, abstractmethod

class Aluno(ABC):
    @abstractmethod
    def media(self):
        pass

    @abstractmethod
    def situacao(self):
        pass

class AlunoRegular(Aluno):
  def __init__(self, notas):
      self.notas = notas

  def media(self):
    return sum(self.notas)/len(self.notas)

  def situacao(self):
    media = self.media()
    if media >= 7: return "APROVADO"
    elif media >= 5: return "RECUPERACAO"
    else: return "REPROVADO"

nome = input().strip
notas = list(map(float, input().split()))


aluno = AlunoRegular(notas)

print(f"{aluno.media():.2f}")
print(aluno.situacao())