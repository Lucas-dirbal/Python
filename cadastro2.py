clientes = []

while True:
    print("\n ==MENU==")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\n --- Novo Cadastro --- ")
        nome = input("Qual seu nome ?")
        telefone = input("Qual seu telefone ?")

        cliente = {
            'nome': nome,
            'telefone': telefone
        }

        clientes.append(cliente)
        print("\nCadastro realizado com sucesso !")
    elif opcao == '2':
        print("\n --- Lista de Clientes --- ")
        for cliente in clientes:
            print(f"Nome: {cliente['nome']} - Telefone: {cliente['telefone']}")
    elif opcao == '3':
        print("\nSaindo do sistema...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")