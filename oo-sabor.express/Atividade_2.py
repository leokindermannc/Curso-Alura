class Carro:
    carros=[]

    def __init__(self,modelo,cor,ativo,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        selfativo = False
        Carro.carros.append(self)

    def listar_carros():
        for Carros in Carro.carros:
            print(f'{Carros.modelo} | {Carros.cor} | {Carros.ano}')
            

carro1 = Carro('Sedan','Vermelho','','2000')
Carro.listar_carros()

class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria,ativo,cidade,preco):
        self.nome = nome
        self.categoria = categoria
        self.cidade = cidade
        self.preco = preco
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def listar_Restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.cidade} | {restaurante.preco} |')
    


restaurante1 = Restaurante('Rover','Italiana','','Criciuma','R$50')
Restaurante.listar_Restaurante()

class CLiente:
    clientes=[]

    def __init__(self,nome,idade,ativo,cidade,RG):
        self.nome = nome
        self.idade = idade
        self.ativo = False
        self.cidade = cidade
        self.RG = RG
        CLiente.clientes.append(self)
