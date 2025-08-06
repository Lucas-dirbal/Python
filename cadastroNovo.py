usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("Lista de usuarios cadastrados:")
    for i, u in enumerate(usuarios):
        
