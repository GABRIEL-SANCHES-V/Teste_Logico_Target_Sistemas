import os

def run_questao_3 ():
    while True:
        os.system("clear")

        indice = 12
        soma = 0
        k = 1

        while k <= indice:
            k = k + 1
            soma = soma + k

        print(f"A soma dos {indice} primeiros números inteiros positivos é {soma}")

        input_continue = input("Deseja refazer? (s/n): ")

        if input_continue.lower() == "n":
            break
