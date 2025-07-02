class Cliente:
    def __init__(self,compra):
        self.compra = compra
        self.desconto = 0
    
    def descontar(self):
        return self.compra * (1 - self.desconto * 0.01)

class ClienteRegular(Cliente):
    def __init__(self,compra):
        super().__init__(compra)
        self.desconto = 5 if compra > 100 else 0

class ClienteVIP(Cliente):
    def __init__(self,compra):
        super().__init__(compra)
        self.desconto = 15 if compra > 200 else 10 if compra > 50 else 0

class ClientePremium(Cliente):
    def __init__(self,compra):
        super().__init__(compra)
        self.desconto = 15

TIPOS = {
    1: ClienteRegular,
    2: ClienteVIP,
    3: ClientePremium,
}

tipo = int(input())
compra_input = float(input())

compra = TIPOS[tipo](compra_input)

print(f"{compra.descontar():.2f}")