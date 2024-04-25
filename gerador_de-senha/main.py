import random
import string
from time import strftime

def gerar_senha(tamanho):
    caracteres = list(string.ascii_letters + string.digits + string.punctuation)

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))

    return senha

def mostra_senha():
    with open("senhas_salvas.txt", "r") as senhas_salvas:
        print(senhas_salvas.read())

def salva_senha(senha):
    tempo = strftime('%d/%m/%Y as %H:%M')

    with open("senhas_salvas.txt", "a", encoding="latin_1") as senhas_salvas:

        senhas_salvas.write(f"Senha: {senha} Criada em {tempo}\n")

    return senha


while True:
    print( "[G]: Digite 0 para finalizar o programa.")
    print("[G]: Digite 1 para escolher o tamanho que sua senha terá.")
    print("[G]: Digite 2 para ver sua(s) senha(s) salva(s).\n")
    opcao = int(input( "[U]: "))

    if opcao == 0:
        break
    elif opcao == 1:
        tamanho = int(input("[U]: "))

        if tamanho == 0:
            pass

        elif tamanho != 0:
            senha = gerar_senha(tamanho)
            salva_senha(senha)
            print("\n", f"Aqui esta sua senha: {senha}\n")

    elif opcao == 2:
        mostra_senha()

