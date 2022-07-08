class Historico_Vendas:
    def __init__(self):
        self.historico = []

    def historico_vendas(self):
        print('-=-=-=-=-= Seu historico de Vendas: -=-=-=-=-=')
        for i in self.historico:
            print('-', i)