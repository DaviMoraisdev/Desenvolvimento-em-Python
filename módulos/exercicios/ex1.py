# Estrutura escolhida: lista de dicionários.
# Motivo: nome não é identificador estável; lista facilita iteração e futura migração para banco de dados.
estoque = [
    {"nome": "Arroz 5kg",    "quantidade": 50,  "preco": 24.90},
    {"nome": "Feijão 1kg",   "quantidade": 120, "preco":  8.75},
    {"nome": "Azeite 500ml", "quantidade": 30,  "preco": 32.50},
]

opcao = ""

while opcao != "4":
    print("\n===== SISTEMA DE CONTROLE DE ESTOQUE =====")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    print("==========================================")

    opcao = input("Digite a opcao desejada: ")

    if opcao == "1":
        # Itera sobre todos os produtos e exibe nome, quantidade e preço formatado
        print("\n---------- ESTOQUE ATUAL ----------")
        for produto in estoque:
            print(f"Produto : {produto['nome']}")
            print(f"  Quantidade : {produto['quantidade']} unidades")
            print(f"  Preço      : R$ {produto['preco']:.2f}")
            print("-----------------------------------")

    elif opcao == "2":
        print("\n------ REGISTRAR ENTRADA ------")
        nome_buscado = input("Nome do produto: ").strip()

        # Busca case-insensitive para evitar falha por diferença de maiúsculas
        produto_encontrado = None
        for produto in estoque:
            if produto["nome"].lower() == nome_buscado.lower():
                produto_encontrado = produto
                break

        if produto_encontrado is None:
            print("Produto não encontrado.")
        else:
            quantidade_entrada = int(input(f"Quantidade a adicionar em '{produto_encontrado['nome']}': "))
            produto_encontrado["quantidade"] += quantidade_entrada
            print(f"Estoque atualizado! '{produto_encontrado['nome']}' agora tem {produto_encontrado['quantidade']} unidades.")

    elif opcao == "3":
        print("\n------ REGISTRAR SAÍDA ------")
        nome_buscado = input("Nome do produto: ").strip()

        # 1ª validação: verifica se o produto existe no estoque
        produto_encontrado = None
        for produto in estoque:
            if produto["nome"].lower() == nome_buscado.lower():
                produto_encontrado = produto
                break

        if produto_encontrado is None:
            print("Produto não encontrado.")
        else:
            quantidade_solicitada = int(input(f"Quantidade a retirar de '{produto_encontrado['nome']}': "))

            # 2ª validação: verifica se há saldo suficiente antes de deduzir
            # Impede que o estoque fique negativo, o que seria um estado inválido
            if quantidade_solicitada > produto_encontrado["quantidade"]:
                print(f"Estoque insuficiente. Disponível: {produto_encontrado['quantidade']} unidades.")
            else:
                produto_encontrado["quantidade"] -= quantidade_solicitada
                print(f"Saída registrada! '{produto_encontrado['nome']}' agora tem {produto_encontrado['quantidade']} unidades.")

    elif opcao == "4":
        # Encerramento explícito com mensagem de despedida
        print("\nSistema encerrado. Até logo!")
        break

    else:
        # Captura qualquer entrada fora do intervalo esperado
        print("Opção inválida. Digite um número entre 1 e 4.")