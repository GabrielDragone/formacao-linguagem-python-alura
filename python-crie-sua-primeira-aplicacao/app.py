import os

# Lista:
restaurantes = []

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
    #os.system('cls') # limpar a tela
    # print('\033c')
    print("Encerrando o programa")

def opcao_invalida():
    print("Opção inválida!")
    digite_para_voltar_ao_menu()


def digite_para_voltar_ao_menu():
    input("Digite qualquer coisa para voltar ao menu principal: ")
    main()


def cadastrar_novo_restaurante():
    #pass # Se uma função não tem implementação, vai ficar com erro. Colocando pass vai ignorar.
    print("Cadastro de novos restaurantes\n")
    novo_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(novo_restaurante) # pra adicionar na lista
    print(f"O restaurante {novo_restaurante} foi cadastrado com sucesso! \n")
    digite_para_voltar_ao_menu()

def listar_restaurantes():
    print(f"Listando restaurantes cadastrados: {restaurantes}")
    digite_para_voltar_ao_menu()

def escolher_opcao_com_if():
    try:
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
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        print("Error print")
        opcao_invalida()

def escolher_opcao_com_match():
    try:
        opcao_escolhida = int(input("Escolha uma opção:"))

        # Exemplo match:
        match opcao_escolhida:
            case 1:
                print("Cadastrar restaurante")
            case 2:
                print("Listar restauranter")
            case 3:
                print("Ativar restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        print("Error match")
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao_com_if()
    # escolher_opcao_com_match()

if __name__ == '__main__':
    main()