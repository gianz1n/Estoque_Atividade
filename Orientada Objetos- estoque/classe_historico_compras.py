class Historico_Compras:
    def __init__(self):
        self.historico = []

    def historico_compras(self):
        print('-=-=-=-=-= Seu historico de compras: -=-=-=-=-=')
        for i in self.historico:
            print('-', i)