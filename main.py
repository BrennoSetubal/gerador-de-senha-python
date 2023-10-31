import random
import string


def gerar_senha(tamanho):
    caracteres = list(string.ascii_letters + string.digits + string.punctuation)

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))

    return senha


while True:
    print("[G]: Digite 0 para finalizar o programa.")
    print("[G]: Digite 1 para escolher o tamanho que sua senha terá.\n")
    opcao = int(input("[U]: "))

    if opcao == 0:
        break
    elif opcao == 1:
        tamanho = int(input("[U]: "))
        senha = gerar_senha(tamanho)
        print("\n", f"Aqui esta sua senha: {senha}")
