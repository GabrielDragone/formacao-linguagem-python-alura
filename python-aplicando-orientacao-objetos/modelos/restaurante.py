class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # Altera a primeira letra da palavra para ser maiusculo.
        self._categoria =  categoria.upper() # Todas as letras maisuculas
        self._ativo = False #_ informa que o atributo protegido e não deve ser mexido.

        # Adiciona o objeto dentro da lista:
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Ativo"}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    def alternar_status(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_praca.alternar_status()
# restaurante_praca.nome = "Praça"
# restaurante_praca.categoria = "Gourmet"

restaurante_pizza = Restaurante("pizza express", "Italiana")

# restaurantes = [
#     restaurante_praca,
#     restaurante_pizza
# ]

# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.listar_restaurantes()