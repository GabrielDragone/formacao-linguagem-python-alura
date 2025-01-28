# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
def exercicio_um():
    print("exercicio_um")
    listaNumeros = []

    for i in range(1, 11):
        listaNumeros.append(i)
    print(f"\nLista Números: {listaNumeros}")

    listaNomes = ["Pitoco", "Ágatha", "Larissa", "Dolores"]
    print(f"\nLista Nomes: {listaNomes}")

    listaAno = ["1950", "2025"]
    print(f"\nLista Anos: {listaAno}")

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
def exercicio_dois():
    print("\nexercicio_dois")
    listaNomes = ["Pitoco", "Ágatha", "Larissa", "Dolores"]
    for nome in listaNomes:
        print(f"\n--{nome}")

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
def exercicio_tres():
    print("\nexercicio_tres")
    calculo = 0
    for i in range(1, 11): #for i in range(1, 11, 2): da pra fazer assim tbm, pulando de 2 em 2 começando com 1.
        if i % 2 == 1:
            calculo += i
    print(f"Resultado: {calculo}")

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
def exercicio_quatro():
    print("\nexercicio_quatro")
    for i in range(10, 0, -1): #10 valor inicial da iteração, 0 valor final e -1 decremento a cada iteração
        print(f"{i}")

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
def exercicio_cinco():
    print("\nexercicio_cinco")
    numero_informado = int(input("Informe um número: "))
    print(f"Tabuada do {numero_informado}")

    for i in range (1, 11):
        print(f"{numero_informado} x {i} = {numero_informado * i}")

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
def exercicio_seis():
    print("\nexercicio_seis")
    lista_de_numeros = []
    numero = 0
    while numero >= 0:
        try:
            numero = int(input("Informe um número positivo: "))
            if numero >= 0:
                lista_de_numeros.append(numero)
        except:
            print("Valor inválido informado!")
            lista_de_numeros.append(0)

    total = 0
    for numero_iterado in lista_de_numeros:
        total += numero_iterado

    print(f"Total calculado: {total}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
def exercicio_sete():
    print("\nexercicio_sete")
    lista_de_numeros = []
    numero = 0
    total = 0
    media = 0

    while numero >= 0:
        try:
            numero = int(input("Informe um número positivo: "))
            if numero >= 0:
                lista_de_numeros.append(numero)
        except:
            print("Valor inválido informado!")

    for numero_iterado in lista_de_numeros:
        total += numero_iterado

    try:
        media = total / len(lista_de_numeros)
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    print(f"Média calculada: {media}")

def main():
    # exercicio_um()
    # exercicio_dois()
    # exercicio_tres()
    # exercicio_quatro()
    # exercicio_cinco()
    # exercicio_seis()
    exercicio_sete()

if __name__ == '__main__':
    main()