import os
import src

def run():

    while True:
        os.system("clear")
        print("1 - Questão 1")
        print("2 - Questão 2")
        print("3 - Questão 3")
        print("0 - Sair\n")

        try:
            input_option = int(input("Digite a questão que deseja executar: "))

            match input_option:
                case 1:
                    src.run_questao_1()
                    continue

                case 2:
                    src.run_questao_2()
                    continue

                case 3:
                    src.run_questao_3()
                    continue

                

                case 0:
                    os.system("clear")
                    print("\nSaindo...")
                    break


                case _:
                    os.system("clear")
                    print("Por favor, insira uma opção válida.")
                    continue

        except ValueError:
            print("Por favor, insira um número válido.")
            continue

run()