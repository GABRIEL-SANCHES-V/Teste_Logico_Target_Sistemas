import os
import platform

def read_string():
    while True:
        input_string = input("Digite uma string: ")

        if not input_string:
            print("Por favor, insira uma string válida.")
            continue

        if not isinstance(input_string, str):
            print("Por favor, insira uma string válida.")
            continue

        break

    return input_string

def checa_ocorrencia(string, letter):

    return string.lower().count(letter.lower())

def run_questao_2():
    while True:
        os.system("clear")
        input_string = read_string()
        input_letter = input("Digite uma letra: ")

        if not isinstance(input_letter, str) or len(input_letter) > 1:
            print("Por favor, insira uma letra válida.")
            continue

        occurrence = checa_ocorrencia(input_string, input_letter)

        print()
        print(f"A letra '{input_letter}' aparece {occurrence} vezes na string '{input_string}'")
        print()

        input_continue = input("Deseja continuar? (s/n): ")

        if input_continue.lower() == "n":
            break