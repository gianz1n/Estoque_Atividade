from classe_produtos import *
from classe_fabricante import *


class Estoque:
    def __init__(self):
        self.lista_de_produtos = []
        self.lista_de_fabricantes = []

    def cadastrar_produtos(self):
        entrada_cod = str(input('Informe o código: ')).strip()
        entrada_nome = str(input('Informe o nome do produto: ')).strip()
        entrada_fabricante = str(input('Informe o nome do fabricante: ')).strip().upper()
        for i in range(len(self.lista_de_fabricantes)):
            if entrada_fabricante == self.lista_de_fabricantes[0].nome:
                self.lista_de_produtos.append(Produto(cod=entrada_cod, nome=entrada_nome, fabricante=entrada_fabricante, quantidade=0))
            else:
                print('Fabricante não cadastrado')

    def listar_produtos(self):
        op_filtro = str(input('Entre com codigo do produto / Clique enter para listar todos: ')).strip()
        if op_filtro == '':
            for i in range(len(self.lista_de_produtos)):
                print(f'\nCOD: {self.lista_de_produtos[i].cod}\nNOME: {self.lista_de_produtos[i].nome}\nFABRICANTE: {self.lista_de_produtos[i].fabricante}\n'
                      f'QUANTIDADE: {self.lista_de_produtos[i].quantidade}')
        else:
            for i in range(len(self.lista_de_produtos)):
                if self.lista_de_produtos[i].cod == op_filtro:
                    print(
                        f'\nCOD: {self.lista_de_produtos[i].cod}\nNOME: {self.lista_de_produtos[i].nome}\nFABRICANTE: {self.lista_de_produtos[i].fabricante}\n'
                        f'QUANTIDADE: {self.lista_de_produtos[i].quantidade}')
                else:
                    pass
    def alterar_descricao(self):
        cod_alterar = str(input('\nDigite o codigo do produto que deseja alterar a descrição: '))
        for i in range(len(self.lista_de_produtos)):
            if self.lista_de_produtos[i].cod == cod_alterar:
                novo_nome = str(input('Digite o novo nome (DESCRIÇÃO): '))
                self.lista_de_produtos[i].nome = novo_nome
                print(f'Nome alterado para {novo_nome}')
            else:
                cont = 0
                cont += 1
                if cont == len(self.lista_de_produtos):
                    print('Codigo não cadastrado')
                else:
                    pass

    def cadastrar_fabricante(self):
        entrada_codigo = str(input('Informe o código: ')).strip()
        fabricante_nome = str(input('Informe o nome: ')).strip().upper()
        self.lista_de_fabricantes.append(Fabricante(cod=entrada_codigo, nome=fabricante_nome))
        print(f'Voce cadastrou o Fabricante {fabricante_nome} com sucesso! ')