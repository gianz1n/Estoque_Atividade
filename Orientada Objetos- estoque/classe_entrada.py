from classe_estoque import *
from classe_historico_compras import *

class Compra:
    def __init__(self):
        self.entrada = Estoque()
        self.historico = Historico_Compras()

    def comprar(self):
        controle = str(input('Digite o codigo do produto: '))
        for i in range(len(self.entrada.lista_de_produtos)):
            if controle == self.entrada.lista_de_produtos[i].cod:
                quantidade = int(input('Informe a quantidade que deseja comprar: '))
                self.entrada.lista_de_produtos[i].quantidade += quantidade
                self.historico.historico.append(f'Compra de {quantidade} itens do produto: {self.entrada.lista_de_produtos[i].nome}, COD: {self.entrada.lista_de_produtos[i].cod}')
            else:
                print('COD não encontrado. ')


