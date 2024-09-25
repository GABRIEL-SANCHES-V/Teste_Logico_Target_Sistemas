import os

def fibonacci(number, lista=None):
    if lista is None:
        lista = set()

    if number == 0:
        lista.add(0)
        return 0
    elif number == 1:
        lista.add(1)
        return 1
    else:
        fib = fibonacci(number - 1, lista) + fibonacci(number - 2, lista)
        lista.add(fib)
        return fib


def run_questao_1():
    while True:

        lista = set()

        os.system("clear")

        input_number = int(input("Digite um número: "))
        fibonacci(input_number + 1, lista)

        lista = sorted(list(lista))

        if input_number in lista or input_number == 0:
            message = f"O número {input_number} pertence à sequência de Fibonacci"
        
        else:
            message = f"O número {input_number} não pertence à sequência de Fibonacci"
        
        print()
        print(message)
        print()

        input_continue = input("Deseja continuar? (s/n): ")

        if input_continue.lower() == "n":
            break
