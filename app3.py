#3o exercício

def check(usuario, senha):
    if usuario == "Admisso" and senha == "patinho":
        print("Acesso permitido.")
    else:
        print("Os nomes de usuário e senha não correspondem.")

print("Digite o nome de usuário:")
usuario = input()
print("Digite a senha:")
senha = input()

check(usuario, senha)
