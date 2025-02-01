class Musica:

    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

        Musica.musicas.append(self)

    def __str__(self):
        return f"Música: {self.nome} | Artista: {self.artista} | Duração: {self.duracao}"

    def listar_musicas():
        print("Listando músicas....")
        for musica in Musica.musicas:
            print(f"Música: {musica.nome} | Artista: {musica.artista} | Duração: {musica.duracao}")


# musica1 = Musica()
# musica1.nome = "Everlong"
# musica1.artista = "Foo Fighters"
# musica1.duracao = 302
# print(vars(musica1))

musica1 = Musica("Everlong", "Foo Fighters", 302)
print(musica1)

# musica2 = Musica()
# musica2.nome = "Miss you"
# musica2.artista = "Oliver Tree"
# musica2.duracao = 245

musica2 = Musica(nome="Miss you", artista="Oliver Tree", duracao=245)
print(musica2)

Musica.listar_musicas()