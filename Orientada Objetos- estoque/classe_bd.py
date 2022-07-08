import mysql.connector
from classe_fabricante import *
from classe_produtos import *
from classe_entrada import *
from classe_historico_compras import *
from classe_historico_vendas import *
import datetime



class Banco_de_Dados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='Estoque')

        self.meu_cursor = self.conexao.cursor()

#cadastro fabricante
    def cadastrar_fabricante(self, cod, nome):
        objeto_fabricante = Fabricante(cod, nome)
        comando_sql = f'insert into Fabricante' \
                      f'(nome_fabricante) ' \
                      f'value ("{objeto_fabricante.nome}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

#cadastro produtos - CREATE
    def cadastrar_produto(self, cod, nome, fabricante, quantidade):
        objeto_produto = Produto(cod, nome, fabricante, quantidade)
        comando_sql = f'select nome_fabricante from Fabricante'
        self.meu_cursor.execute(comando_sql)
        luisa = self.meu_cursor.fetchall()
        for i in luisa:
            estoque1 = str(i)
            estoque1.replace(',', '')
            estoque2 = estoque1.replace('(', '')
            estoque3 = estoque2.replace(')', '')
            estoque4 = estoque3.replace(',', '')
            if fabricante in estoque4:
                comando_sql = f'insert into Produto (nome_produto, fabricante_produto, quantidade_produto) value ("{objeto_produto.nome}", "{objeto_produto.fabricante}", {objeto_produto.quantidade})'
                self.meu_cursor.execute(comando_sql)
                self.conexao.commit()
                break
            else:
                pass
        else:
            pass

#listar produtos
    def listar_produto(self, cod):
        if cod == '':
            self.meu_cursor.execute(f'select * from Produto')
            lista = self.meu_cursor.fetchall()
            for i in lista:
                print(i)
        else:
            comando_sql = f'select * from Produto'
            self.meu_cursor.execute(comando_sql)
            lista = self.meu_cursor.fetchall()
            for i in lista:
                print(i)

#alterar nome
    def alterar_nome(self, atributo, valor, cod):
        comando_sql = f'update Produto set {atributo} = "{valor}" where cod_produto {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

#comprar produtos
    def comprar_produtos(self, atributo, cod, quantidade):
        comando_sql = f'update Produto set {atributo} = quantidade_produto + {quantidade} where cod_produto = {cod}'
        data = datetime.date.today()
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()
        historico_compra = Historico_Compras()
        comando_compra = f'insert into Historico_compra (cod_produto_hc, data_hc, quantidade_hc) value("{cod}", "{data}", "{quantidade}")'
        self.meu_cursor.execute(comando_compra)
        self.conexao.commit()

#vender produtos
    def vender_produtos(self, cod, atributo, quantidade_final):
        self.meu_cursor.execute(f'select (quantidade_produto) from Produto where cod_produto = {cod}')
        lista = self.meu_cursor
        for i in lista:
            estoque1 = str(i)
            estoque1.replace(',', '')
            estoque2 = estoque1.replace('(', '')
            estoque3 = estoque2.replace(')', '')
            estoque4 = estoque3.replace(',', '')
            estoque5 = int(estoque4)
            if quantidade_final <= estoque5:
                comando_sql = f'update Produto set {atributo} = quantidade_produto - {quantidade_final} where cod_produto = {cod}'
                data = datetime.date.today()
                self.meu_cursor.execute(comando_sql)
                self.conexao.commit()
                print('Venda realizada!')
                historico_venda = Historico_Vendas()
                comando_venda = f'insert into Historico_venda (cod_produto_hv, data_hv, quantidade_hv) value("{cod}", "{data}", "{quantidade_final}")'
                self.meu_cursor.execute(comando_venda)
                self.conexao.commit()
            else:
                print('Quantidade indisponível para venda!')

    def listar_historico_compra(self):
        comando_sql = f'select * from Historico_compra'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print('Id historico: ', i[0],
                  'Cod produto: ', i[1],
                  'Data: ', i[2],
                  'Quantidade produto: ', i[3])

    def listar_historico_venda(self):
        comando_sql = f'select * from Historico_venda'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print('Id historico: ', i[0],
                  'Cod produto: ', i[1],
                  'Data: ', i[2],
                  'Quantidade produto: ', i[3])







