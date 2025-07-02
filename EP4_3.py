from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
      pass

class Horista(Funcionario):
   def __init__(self,salario):
      self.salario=salario

   def calcular_salario(self):
      return f"{(self.salario[0]*self.salario[1]):.2f}"

class Mensalista(Funcionario):
   def __init__(self,salario):
      self.salario=salario

   def calcular_salario(self):
      return f"{self.salario[0]:.2f}"
   
TIPO = {
   "Mensalista": Mensalista,
   "Horista": Horista
}
  
nome=input()
tipo=input()
salario=list(map(float, input().split()))
funcionario=TIPO[tipo](salario)
print(funcionario.calcular_salario())
