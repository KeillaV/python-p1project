def menu_inicial():
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\n1 - Cadastrar produtos \n2 - Listar produtos \n3 - Abrir o caixa \n4 - Sair \n")
    opcao = int(input("Por favor, escolha uma das opções acima: "))

    while (opcao < 1) or (opcao > 4):
        opcao = int(input("Opção inválida! Digite novamente: "))

    return opcao


def cadastro_produto(matriz):
    produto = []

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    codigo = input("Digite o código do produto: ")

    indice = 0

    # Confirmando se o código digitado é novo:
    while (indice < len(matriz)):
        if (codigo == matriz[indice][0]):
            codigo = input("O código digitado já está cadastrado! Digite um novo código: ")
            # Reiniciar contador:
            indice = 0
        else:
            indice += 1

    nome = input("Digite o nome do produto: ").strip().capitalize()
    preco = float(input("Digite o preço: "))

    print("\n-----------------------------------------------------------------")
    print("Código: {} | Nome: {} | Preço: R$ {:.2f}".format(codigo, nome, preco))
    print("-----------------------------------------------------------------\n")

    produto.append(codigo)
    produto.append(nome)
    produto.append(preco)

    return produto


def dados_produto(matriz):
    produto = []

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    codigo = input("Digite o código do produto: ")

    codigo_naoencontrado = True

    for info_produto in matriz:
        if (codigo == info_produto[0]):
            # Descobrindo a posição do código na matriz, é possível descobrir a posição do nome e do preço:
            nome = info_produto[1]
            preco = float(info_produto[2])
            codigo_naoencontrado = False


    # Se não encontrar o código na matriz:
    while codigo_naoencontrado:
        codigo = input("Código não encontrado! Digite novamente: ")

        for info_produto in matriz:
            if (codigo == info_produto[0]):
                # Descobrindo a posição do código na matriz, é possível descobrir a posição do nome e do preço:
                nome = info_produto[1]
                preco = float(info_produto[2])
                codigo_naoencontrado = False

    quant = int(input("Digite a quantidade: "))

    print("\n-----------------------------------------------------------------")
    print("Código: {} | Nome: {} | Preço: R$ {:.2f} | Quantidade: {} ".format(codigo, nome, preco, quant))
    print("-----------------------------------------------------------------")

    total = preco * quant

    produto.append(codigo)
    produto.append(nome)
    produto.append(preco)  # Preço unitário
    produto.append(quant)
    produto.append(total)  # Preço total do produto

    return produto


def nota_fiscal(continuar, arquivo_compra, total_a_pagar):
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Código |  Produto   | Preço (uni) | Quantidade | Preço total")

    for produto in arquivo_compra:
        print("  {}   |    {}    |   R$ {:.2f}   |     {}      | R$ {:.2f}".format(produto[0], produto[1], produto[2],
                                                                                   produto[3], produto[4]))
    print("-----------------------------------------------------------------\n")

    if (continuar == 2):
        print("                                         Total a pagar: R$ {:.2f}".format(total_a_pagar))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")


# Os dados da matriz estão registrados em um arquivo de texto!
# 'encoding': Para o Python reconhecer os acentos do arquivo
produtos = open("Produtos.txt", "r", encoding='utf-8')

# Matriz de n linhas e 3 colunas (Código, nome e preço do produto):
matriz_produtos = []

dados = produtos.readlines()

for indice in range(len(dados)):
    matriz_produtos.append(dados[indice].split())

produtos.close()

opcao = menu_inicial()

while (opcao != 4):

    if (opcao == 1):
        # Função de cadastrar produtos:
        continuar = 1

        while (continuar == 1):
            produto = cadastro_produto(matriz_produtos)

            confirmar = int(input("As informações digitadas estão corretas? \n1 - Sim | 2 - Não\n"))

            while (confirmar > 2) or (confirmar < 1):
                confirmar = int(input("As informações digitadas estão corretas? \n1 - Sim | 2 - Não \n"))

            while (confirmar == 2):
                produto = cadastro_produto(matriz_produtos)
                confirmar = int(input("As informações digitadas estão corretas? \n1 - Sim | 2 - Não \n"))

                while (confirmar > 2) or (confirmar < 1):
                    confirmar = int(input("As informações digitadas estão corretas? \n1 - Sim | 2 - Não \n"))

            matriz_produtos.append(produto)

            produtos = open("Produtos.txt", "a")
            produtos.write("\n")
            for dado in produto:
                produtos.write(str(dado) + " ")

            produtos.close()

            continuar = int(input("\nContinuar cadastrando? \n1 - Sim | 2 - Não \n"))

            while (continuar < 1) or (continuar > 2):
                continuar = int(input("\nContinuar cadastrando? \n1 - Sim | 2 - Não \n"))

            print("\n\n")

        opcao = menu_inicial()


    elif (opcao == 2):
        # Função de listar produtos:
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Código |   Produto   | Preço (uni) ")
        for info_produto in matriz_produtos:
            print("   {}  |    {}    |  R$ {:.2f}   ".format(info_produto[0], info_produto[1], float(info_produto[2])))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")

        opcao = menu_inicial()


    elif (opcao == 3):
        # Função de abrir caixa:

        # Matriz de n linhas e 5 colunas (Código, nome, preço unitário, quantidade e preço total do produto):
        compra = []
        total = 0

        continuar = 1

        while (continuar == 1):
            produto_confirm = dados_produto(matriz_produtos)

            confirmar = int(input("\nAs informações acima estão corretas? \n1 - Sim | 2 - Não \n"))

            while (confirmar > 2) or (confirmar < 1):
                confirmar = int(input("As informações acima estão corretas? \n1 - Sim | 2 - Não \n"))

            while (confirmar == 2):
                produto_confirm = dados_produto(matriz_produtos)

                confirmar = int(input("\nAs informações acima estão corretas? \n1 - Sim | 2 - Não \n"))

            preco_confirm = produto_confirm[2]
            quant = produto_confirm[3]
            total_produto = produto_confirm[4]

            total += total_produto

            compra.append(produto_confirm)

            nota_fiscal(continuar, compra, total)

            continuar = int(input("1 - Inserir novo produto | 2 - Encerrar compra \n"))

            while (continuar < 1) or (continuar > 2):
                continuar = int(input("1 - Inserir novo produto | 2 - Encerrar compra \n"))

        nota_fiscal(continuar, compra, total)

        opcao = menu_inicial()
