class Empregado:
    def __init__(self,cargo,salario,bonus):
        self.cargo = cargo
        self.salario = salario
        self.bonus = bonus

    def calcularSalario(self):
        return self.salario + self.bonus

class Gerente(Empregado):
    def __init__(self,cargo,salario,bonus):
        super().__init__(cargo,salario,bonus/12)

class Vendedor(Empregado):
    def __init__(self,cargo,salario,bonus):
        super().__init__(cargo,salario,bonus*0.05)

CARGO = {
    "E": Empregado,
    "G": Gerente,
    "V": Vendedor
}

i = int(input())
for _ in range(i):
    dados = input().split()
    cargo = dados[0]
    nome = dados[1]
    salario_base = float(dados[2])
    bonus = float(dados[3]) if len(dados) > 3 else 0
    
    empregado = CARGO[cargo](cargo, salario_base, bonus)

    print(f"Nome: {nome} Salario: {empregado.calcularSalario():.2f}")

