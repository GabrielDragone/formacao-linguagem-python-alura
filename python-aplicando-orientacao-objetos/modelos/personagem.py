class Personagem():
    personagens = []

    def __init__(self, nome, raca, nivel_poder):
        self.id = len(Personagem.personagens) + 1
        self.nome = nome
        self.raca = raca
        self.nivel_poder = nivel_poder
        Personagem.personagens.append(self)

    def listar_personagens(ordenar_por=None, reverso=False):
        if ordenar_por:
            print(f"\nListando Personagens por {ordenar_por} {reverso}:")
            # key: Parametro que indica por qual campo o sorted será ordenado.
            # lambda: É uma função anonima (sem nome) e simples, criada na hora que vai receber um objeto p (cada personagem na lista).
            # getattr: É uma função do python que pega o valor de um atributo do objeto passado para ser ordenado.
            personagens_ordenados = sorted(Personagem.personagens, key=lambda p: getattr(p, ordenar_por), reverse=reverso)
        else:
            print("\nListando Personagens:")
            personagens_ordenados = Personagem.personagens

        for personagem in personagens_ordenados:
            print(f"{personagem.id} - {personagem._nome} da raça {personagem.raca} com poder de luga de {personagem.nivel_poder}")


goku = Personagem("Goku", "Sayajin", 9000)
vegeta = Personagem("Vegeta", "Sayajin", 8000)
kurilin = Personagem("Kurilin", "Humano", 500)
piccolo = Personagem("Piccolo", "Namekuseijin", 4000)
majin_buu = Personagem("Majin-Buu", "Majin", 9500)

# Listar personagens ordenados por nível de poder (do menor para o maior)
Personagem.listar_personagens(ordenar_por="nivel_poder")

# Listar personagens ordenados por nível de poder (do maior para o menor)
Personagem.listar_personagens(ordenar_por="nivel_poder", reverso=True)

# Listar personagens ordenados por id (do maior para o menor)
Personagem.listar_personagens(ordenar_por="id", reverso=True)

# Listar personagens ordenados por nome (do maior para o menor)
Personagem.listar_personagens(ordenar_por="nome", reverso=True)

# Listar personagens sem ordenação
Personagem.listar_personagens()


