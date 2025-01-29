def exibir_subtitulo(texto):
    linha = "*" * (len(texto)) # Colocar vários * no tamanho do texto
    print()
    print(linha)
    print(texto)
    print(linha)
    print()

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
def exercicio_um():
    exibir_subtitulo('Exercicio 01')
    pessoa = criar_pessoa()
    print(pessoa)

def criar_pessoa():
    pessoa = {
        'nome': 'João',
        'idade': 15,
        'cidade': 'Curitiba'
    }
    return pessoa

# 2 - Utilizando o dicionário criado no item 1:
def exercicio_dois():
    exibir_subtitulo('Exercicio 02')
    pessoa = criar_pessoa()

    # Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    pessoa['cidade'] = 'São Paulo'
    print(pessoa)

    # Adicione um campo de profissão para essa pessoa:
    pessoa['profissao'] = 'Desenvolvedor'
    print(pessoa)

    # Remova um item do dicionário.
    del pessoa['idade'] # Remove o item
    print(pessoa)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5:
def exercicio_tres():
    exibir_subtitulo('Exercicio 03')

    quadrados = {}
    for i in range(1, 6):
        quadrados[i] = i * i

    print(quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
def exercicio_quatro():
    exibir_subtitulo('Exercicio 04')

    pessoa = criar_pessoa()

    # chave = 'idade'  # Existe
    chave = 'genero' # Não existe

    if chave in pessoa:
        print(f"A chave '{chave}' existe no dicionário!")
    else:
        print(f"A chave '{chave}' não existe no dicionário!")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
def exercicio_cinco():
    exibir_subtitulo('Exercicio 05')

    frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos do."
    contagem_palavras = {}
    palavras = frase.split()
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    print(contagem_palavras)

def main():
    exercicio_um()
    exercicio_dois()
    exercicio_tres()
    exercicio_quatro()
    exercicio_cinco()

if __name__ == '__main__':
    main()