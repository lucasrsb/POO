from abc import ABC, abstractmethod

class Tarefa(ABC):
  @abstractmethod
  def executar():
    pass

class TarefaSimples:
  def __init__(self,msg):
    self.msg=msg

  def executar(self):
    return f"{self.msg} concluída."
  
msg = input()
msg = TarefaSimples(msg)
print(msg.executar())