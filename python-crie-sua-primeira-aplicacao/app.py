import os

# Lista:
# restaurantes = ["Pizza Boy", "Sushi Girl"]
restaurantes = [
    { 'nome': 'Pizza Boy', 'categoria': 'Pizzaria', 'ativo': True },
    { 'nome': 'Sushi Girl', 'categoria': 'Japonesa', 'ativo': False },
    { 'nome': 'Paineiras', 'categoria': 'Tradicional', 'ativo': False },
]

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
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    #os.system('cls') # limpar a tela
    # print('\033c')
    print("Encerrando o programa")

def opcao_invalida():
    print("Opção inválida!")
    digite_para_voltar_ao_menu()

def digite_para_voltar_ao_menu():
    input("\nTecle ENTER para voltar ao menu principal")
    main()

def cadastrar_novo_restaurante():
    #pass # Se uma função não tem implementação, vai ficar com erro. Colocando pass vai ignorar.
    exibir_subtitulo("Cadastro de novos restaurantes")
    novo_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input("Digite a categoria do novo restaurante: ")

    dados_do_restaurante = {
        'nome': novo_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    # restaurantes.append(novo_restaurante) # pra adicionar na lista
    restaurantes.append(dados_do_restaurante) # pra adicionar na lista
    print(f"O restaurante {novo_restaurante} foi cadastrado com sucesso! \n")
    digite_para_voltar_ao_menu()

def listar_restaurantes():
    # print(f"Listando restaurantes cadastrados: {restaurantes}")
    exibir_subtitulo("Listando restaurantes cadastrados:")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = "Ativado" if restaurante['ativo'] else "Desativado" # if ternário
        # print(f" - {nome_restaurante} | {categoria} | {status}")
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}") # Adicionada formatação usando ljust
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

def alterar_status_restaurante():
    exibir_subtitulo("Alterando o estado do restaurante")

    restaurante_encontrado = False
    nome_restaurante = input("Informe o nome do restaurante para alterar o status: ")

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante['ativo'] = not restaurante['ativo'] # o not faz inverter a situação atual do status
            restaurante_encontrado = True
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante['ativo'] \
                else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado!")

    digite_para_voltar_ao_menu()

def exibir_subtitulo(texto):
    linha = "*" * (len(texto)) # Colocar vários * no tamanho do texto
    print()
    print(linha)
    print(texto)
    print(linha)
    print()

def main():
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao_com_if()
    # escolher_opcao_com_match()
    alterar_status_restaurante()

if __name__ == '__main__':
    main()