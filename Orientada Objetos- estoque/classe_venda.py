from classe_estoque import *
from classe_historico_vendas import *

class Venda:
    def __init__(self):
        self.saida = Estoque()
        self.historico = Historico_Vendas()

    def vender(self):
        controle = str(input('Digite o codigo do produto: '))
        for i in range(len(self.saida.lista_de_produtos)):
            if controle == self.saida.lista_de_produtos[i].cod:
                quantidade = int(input('Informe a quantidade que deseja vender: '))
                if self.saida.lista_de_produtos[i].quantidade >= quantidade:
                    self.saida.lista_de_produtos[i].quantidade -= quantidade
                    self.historico.historico.append(f'Venda de {quantidade} itens do produto: {self.saida.lista_de_produtos[i].nome}, COD: {self.saida.lista_de_produtos[i].cod}')
                else:
                    print('Você não pode realizar esta operação, estoque insuficiente. ')
        else:
            print('COD não encontrado. ')
