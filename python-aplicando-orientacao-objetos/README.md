# formacao-linguagem-python-alura
Curso Alura: Aprenda a programar em Python com Orientação a Objetos

---

### Python: aplicando a Orientação a Objetos:

#### 01. Classes:

* 02 - Classes:
  * Objetivo de aproximar a programação ao mundo real.
  * Temos os moldes que são as classes e objetos que são instâncias dessa classe.
  * Usamos a palavra reservada class para identificar uma classe.
  * Cada objeto encapsula dados e comportamentos relacionados, promove modularidade e possibilita a reutilização de código.
* 03 - Atributos de instância:
  * dir(objeto): mostra os atributos e métodos de uma classe.
  * vars(objeto): mostra o dicionário desses atributos e métodos.

#### 02. Construtor e instanciando objetos:
* 02 - Construtor:
  * __init__(self, parametros) é o método construtor.
  * Definimos dentro da classe.
  * O self é utilizado para indicar ao código que estamos falando de determinado objeto.
* 03 - Métodos especiais:
  * Quando precisamos mostrar o objeto em formato de texto, sem tratar, o python nos mostra a posição do endereço na memória para aquele objeto, criamos o método __str__(self)
  * Quando criamos o método precisamos informar o self para o código entender qual objeto estamos informando para o mesmo manipular. Ele é a referencia da instancia atual que estamos usando no momento.
  * Após criar o str, ao mandarmos imprimir, vai imprimir aquilo que definimos.
  * O self é o nome padrão a ser utilizado, mas podemos chamar de this, objeto, antonio, qualquer coisa.
* 04 - Criando meus métodos:
  * Os métodos especiais (dunder methods) são os que tem underlines na escrita. Entendi como sendo os overrides.
  * Os que estão sem, são os nossos próprios.
* 06 - Mão na massa: refatorando uma função:
  * Refatorando a classe [musica.py](modelos/musica.py).

#### 03. Property e métodos de classe:
* 02 - Property:
  * Modificar como um atributo é lido.
  * @property.
  * Sempre que utilizamos essa anotação, indicamos que queremos modificar como determinado atributo é lido. Método ativo.
  * Utilizado https://coolsymbol.com/ para pegar um simbolo a ser utilizado no property.
  * Quando colocamos um _ na frente de um atributo, estamos informando que esse é protegido e não pode ser acessado direto.
  * Agora ao chamar o ativo (sem _), conseguimos acessar a modificação que fizemos. Chamando com _, fica igual era antes.
* 03 - Aprofundando em propriedades:
  * Nem sempre precisaremos usar properties para todos os valores que temos na aplicação.
  * Podemos usar diretamente funções do proprio Python para nos ajudar, como a title e upper.
  * Ainda falando sobre o _, se usarmos o _ para reatribuir o valor de alguma variavel protegida, iremos conseguir, mas o ideal é que qnd as variaveis estiverem com esse caractere na frente, a gente não altere.
* 04 - Métodos de classe:
  * Quando temos um método que não é referenciado por uma instancia, e sim pela própria classe, uma boa prática é anotamos o método da classe com o decorator @classmethod. Exemplo listar_restaurantes.
  * E é uma convenção utilizarmos o cls como parâmetro no próprio método.
  * E os métodos de instancia, deixamos sem o _ mesmo. Exemplo alternar_status.
* 
