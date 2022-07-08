from classe_bd import *

class Menu:
    estoque = Banco_de_Dados()

    # Iniciar menu
    while True:
            op = input('\n-=-=-=--=-= Informe a opção desejada -=-=-=--=-=\n1 | Cadastros\n2 | Listar Produtos\n3 | Alterar Produto\n4 | Comprar produtos\n5 | Vender produtos\n6 | Historicos\n0 | Sair\n-=-= Sua Escolha: ').strip()

            if op == '1':# OPÇÃO PARA CADASTRAR NOVOS PRODUTOS
                while True:
                    op_cadastro = str(input('\n-=-=-=--=-= Cadastros -=-=-=--=-=\n1 | Cadastrar Produtos\n2 | Cadastrar Fabricantes\n0 | Voltar\n-=-= Sua Escolha: ')).strip()
                    if op_cadastro == '1':
                        quantidade = int(0)
                        cod = None
                        nome = input('Informe o nome do produto: ')
                        fabricante = input('Informe o nome do fabricante: ')
                        produto_quantidade = quantidade
                        estoque.cadastrar_produto(cod, nome, fabricante, produto_quantidade)

                    elif op_cadastro == '2':
                        cod = None
                        fabricante = input('Informe o nome do fabricante: ')
                        estoque.cadastrar_fabricante(cod, fabricante)

                    elif op_cadastro == '0':
                        break

            elif op == '2':# OPÇÃO PARA LISTAR PRODUTOS
                estoque.listar_produto(cod)

            elif op == '3':# OPÇÃO PARA ALTERAR A DESCRIÇÃO DE UM PRODUTO
                cod = input('Digite o código do produto: ')
                valor = input('Digite o novo nome: ')
                atributo = 'nome'
                estoque.alterar_nome(atributo, valor, cod)

            elif op == '4':# OPÇÃO PARA COMPRAS PRODUTOS
                cod = input('Digite o código do produto: ')
                quantidade_comprar = input('Quantidade de produtos a comprar: ')
                quantidade_final = quantidade_comprar
                atributo = 'quantidade_produto'
                estoque.comprar_produtos(atributo, cod, quantidade_final)


            elif op == '5':# OPÇÃO PARA VENDER PRODUTOS
                cod = input('Digite o código do produto: ')
                quantidade_comprar = int(input('Quantidade de produtos a vender: '))
                quantidade_final = quantidade_comprar
                atributo = 'quantidade_produto'
                estoque.vender_produtos(cod, atributo, quantidade_final)

            elif op == '6':
                while True:
                    op_historico = str(input('\n-=-=-=--=-= Historicos -=-=-=--=-=\n1 | Historico Compras\n2 | Historico Vendas\n0 | Voltar\n-=-= Sua Escolha: ')).strip()
                    if op_historico == '1':
                        estoque.listar_historico_compra()
                    elif op_historico == '2':
                        estoque.listar_historico_venda()
                    elif op_historico == '0':
                        break

            elif op == '0':
                print('-=-=-=-=- Agradecemos por utlizar nosso sistema -=-=-=-=-')
                break
            else:
                print('Entrada incorreta')