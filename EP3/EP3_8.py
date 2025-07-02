class Produto():
  def __init__(self, nome, ordem):
    self.nome = nome
    self.ordem = ordem
  
  def __lt__(self, other):
    return int(self.ordem) < int(other.ordem)

  def __str__(self):
    return f"{self.nome}"
  
class ProdutoEletronico(Produto):
  pass

class ProdutoRoupa(Produto):
  TAMANHO = {  'P': 1, 'M': 2, 'G': 3, 'GG': 4}
  def __init__(self,nome,ordem):
    super().__init__(nome,ordem)
    self.ordem = self.TAMANHO[self.ordem]  

TIPO = {'1': ProdutoEletronico, '2': ProdutoRoupa}

tipo = input()

produtos=[]

t = int(input())
for _ in range(t):
  nome, ordem = input().split()
  produtos.append(TIPO[tipo](nome, ordem))

produtos.sort()
print('\n'.join(str(produto) for produto in produtos))



