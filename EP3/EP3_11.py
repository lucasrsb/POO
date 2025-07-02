class Carrinho():
  def inserirItem(self, a, b):
    if isinstance(a, str):
      return f"{a} e {b}"
    total = a+b
    if isinstance(a, float):
      return f"R${total}"
    return total
  
carrinho = Carrinho()
