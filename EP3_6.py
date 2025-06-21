# Desenvolva um sistema para auditoria de veículos. Crie uma classe base Veiculo com atributos placa e anoFabricacao. Adicione um método calcularIPVA() que, por padrão, retorna 0 (0 para veículos que não pagam IPVA). Crie as classes Carro (que herda de Veiculo e tem valorMercado) e Moto (que herda de Veiculo e tem cilindradas). O cálculo do IPVA é:

# Carro: 2.5% do valorMercado se tiver até 20 anos de uso. Se mais de 20 anos, não paga (0).
# Moto: R$ 50.00 fixo + (0.10 * cilindradas) se tiver até 15 anos de uso. Se mais de 15 anos, não paga (0). Seu programa deve ler uma lista de veículos e, ao final, imprimir o valor total do IPVA a ser arrecadado. Assuma que o ano atual é 2025 para o cálculo da idade do veículo.
# Entrada: A entrada começa com um número inteiro N, indicando a quantidade de veículos. As próximas N linhas descrevem os veículos:

# C placa anoFabricacao valorMercado: Para um carro.
# M placa anoFabricacao cilindradas: Para uma moto.
# Saída: Seu programa deve imprimir o valor total do IPVA a ser arrecadado, com 2 casas decimais. 

# C ABC1234 2020 50000.00: Idade = 2025 - 2020 = 5 anos. IPVA = 50000.00 * 0.025 = 1250.00
# M XYZ5678 2023 250: Idade = 2025 - 2023 = 2 anos. IPVA = 50.00 + (0.10 * 250) = 50.00 + 25.00 = 75.00
# C DEF9012 2000 30000.00: Idade = 2025 - 2000 = 25 anos. IPVA = 0.00
# Total IPVA = 1250.00 + 75.00 + 0.00 = 1325.00

class Veiculo():
  def __init__(self, ano, extra):
    self.ano = ano
    self.extra = extra
  
  def calcularIdade(self):
    return 2025 - ano

  def calcularIPVA(self):
    pass 

class Carro(Veiculo):
  def calcularIPVA(self):
    return self.extra * 0.025

class Moto(Veiculo):
  def calcularIPVA(self):
    idade = self.calcularIdade()
    IPVA = 0 if idade > 15 else 50 + (0.1 * self.extra)
    return IPVA

VEICULOS = {
  "C": Carro,
  "M": Moto
}

IPVA = 0

i = int(input())
for _ in range(i):
  dados = input().split()
  tipo = dados[0]
  ano = int(dados[2])
  extra = float(dados[3])

  veiculo = 0 if 2025 - ano > 20 else VEICULOS[tipo](ano, extra)

  IPVA += veiculo.calcularIPVA() if veiculo != 0 else 0

print(f"{IPVA:.2f}")