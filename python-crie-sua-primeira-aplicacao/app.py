import os

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    
    """)

def exibir_menu():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurantes")
    print("4. Sair\n")

def finalizar_app():
    os.system('cls') # limpar a tela
    print("Encerrando o programa")

def escolher_opcao_com_if():
    # Para ler o que o usuário digitou:
    #opcao_escolhida = input("Escolha uma opção:")
    opcao_escolhida = int(input("Escolha uma opção:"))

    #print("Você escolheu a opção:", opcao_escolhida)
    # Interpolação:
    #print(f"Você escolheu a opção: {opcao_escolhida}")

    # Pra ver o tipo da variável:
    #print(type(opcao_escolhida))

    # Exemplos if, else if e else:
    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restauranter")
    elif opcao_escolhida == 3:
        print("Ativar restaurante")
    else:
        finalizar_app()

def escolher_opcao_com_match():
    opcao_escolhida = int(input("Escolha uma opção:"))

    # Exemplo match:
    match opcao_escolhida:
        case 1:
            print("Cadastrar restaurante")
        case 2:
            print("Listar restauranter")
        case 3:
            print("Ativar restaurante")
        case _:
            finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao_com_if()
    # escolher_opcao_com_match()

if __name__ == '__main__':
    main()