def for_example():
    print("\n Executando exemplo FOR:")
    numero = -1
    for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
        numero = int(input("Digite um número positivo: "))
        if numero > 0:
            break
    print("Você digitou:", numero)

def while_example():
    print("\n Executando exemplo WHILE:")
    numero = -1
    while numero <= 0:
        numero = int(input("Digite um número positivo: "))
    print("Você digitou:", numero)

def main():
    for_example()
    while_example()

if __name__ == '__main__':
    main()
