# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
def exercicio_um(idade):
    print("Exercicio 01:")
    if idade % 2 == 0:
        print("Idade par\n")
    else:
        print("Idade impar\n")

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.
def exercicio_dois(idade):
    print("Exercicio 02:")
    print(f"Idade informada: {idade}")

    if 0 <= idade <= 12:
        print("Criança: 0 a 12 anos\n")
    elif 13 <= idade <= 18:
        print("Adolescente: 13 a 18 ano\n")
    elif idade > 18:
        print("Adulto: acima de 18 anos\n")
    else:
        print("Idade inválida\n")

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
def exercicio_tres(tentativa):
    usuario_digitado = input("Digite seu usuario ou digite sair para encerrar o programa: ")
    if usuario_digitado == "sair":
        print("Encerrando o programa")
        return

    senha_digitada = input("Digite sua senha: ")

    usuario = "dragone"
    senha = "123"

    if usuario == usuario_digitado and senha == senha_digitada:
        print("Acessado com sucesso!\n")
    else:
        maximo_tentativas = 3
        if tentativa == 3:
            print("Tentativas de login esgotadas. Tenta novamente mais tarde\n")
        else:
            print(f"Usuário ou senha incorretos. Tente novamente! Tentativas restantes: {maximo_tentativas - tentativa}\n")
            exercicio_tres(tentativa + 1) # recursividade

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.
def exercicio_quatro(x, y):
    # x = int(input("Informe a coordenada x: "))
    # y = int(input("Informe a coordenada y: "))

    if x > 0 and y > 0:
        print("Primeiro Quadrante: os valores de x e y devem ser maiores que zero")
    elif x < 0 and y > 0:
        print("Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero")
    elif x < 0 and y < 0:
        print("Terceiro Quadrante: os valores de x e y devem ser menores que zero")
    elif x > 0 and y < 0:
        print("Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero")
    else:
        print("Caso contrário: o ponto está localizado no eixo ou origem")

def main():
    # idade = int(input("Informe a sua idade: "))
    # exercicio_um(idade)

    # exercicio_dois(-1)
    # exercicio_dois(1)
    # exercicio_dois(12)
    # exercicio_dois(13)
    # exercicio_dois(25)

    # exercicio_tres(0)

    # Primeiro Quadrante:
    exercicio_quatro(5, 3)
    # Segundo Quadrante:
    exercicio_quatro(-2, 4)
    # Terceiro Quadrante:
    exercicio_quatro(-3, -1)
    # Quarto Quadrante:
    exercicio_quatro(1, -5)
    # Caso contrário (origem):
    exercicio_quatro(0, 0)

if __name__ == '__main__':
    main()

