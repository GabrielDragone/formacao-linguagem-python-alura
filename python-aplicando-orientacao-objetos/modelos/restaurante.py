class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria =  categoria
        self.ativo = False

        # Adiciona o objeto dentro da lista:
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante}')

restaurante_praca = Restaurante("Praça", "Gourmet")
# restaurante_praca.nome = "Praça"
# restaurante_praca.categoria = "Gourmet"

restaurante_pizza = Restaurante("Pizza Express", "Italiana")

# restaurantes = [
#     restaurante_praca,
#     restaurante_pizza
# ]

# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.listar_restaurantes()