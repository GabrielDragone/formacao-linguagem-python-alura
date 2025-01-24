# formacao-linguagem-python-alura
Curso Alura: Aprenda a programar em Python com Orientação a Objetos

---

### O que é Python? — um guia completo para iniciar nessa linguagem de programação
* https://www.alura.com.br/artigos/python
* Funciona em uma grande variedade de aplicações diferentes.
* Framework WEB: Django e Flask.
* Datascience e machine learning.
* Linguagem interpretada:
  * Não precisa passar pelo processo de compilação.
  * Processo de interpretação é executado dentro de máquinas virtuais.
* Sintaxe simples.
* Multiparadigma:
  * Diversas maneiras de se programar, orientada a objetos, procedural (instruções transmitidas ao computador na sequência que devem ser excecutadas), funcional (programas construidos aplicando e compondo funções).
* Semântica dinâmica, parecido com Kotlin.
* Vasta biblioteca.
* Guido van Rossun final da década de 1980.
* Download: https://www.python.org/downloads/
* IDEs mais escolhidas para desenvolvimento web s]ao Visual Studio Code e Pycharm.
* Tipos de dados, mas lembrar que é dinamicamente tipada:
  * Int 1
  * Floar 1.1
  * Complex 8j
    * Cálculos geométricos e científicos.
    * Da pra converter um numero real em um numero cmplexo.
  * String hello
  * Boolean true
  * List ['Monica', 'Rachel']
  * Tuple (90, 79, 54, 32)
    * Agrupador de conjunto de elementos.
    * A diferença da lista para tuplas é que tuplas são imutáveis.
  * Dictonary {'Camila': 1.65, 'Larissa': 1.60, 'Guilherme': 1.70}
    * estrutura chave e valor 
* Dá pra fazer conversões de tipos de variáveis.
* Exemplos if, else if e else:
```
media = 6
if media < 5
print(“Você foi reprovado”)
elif media > 5 
media < 7
    print(“Você fará a recuperação”)
else:
    print(“Você foi aprovado”)
```
* Exemplos match:
```
media = 6

match media:
    case media if media < 5:
        print("Você foi reprovado")
    case media if 5 <= media < 7:
        print("Você fará a recuperação")
    case media if media >= 7:
        print("Você foi aprovado")
```
* Exemplo de estruturas de repetição: for e while:
```
for i in range(1,10):
    print(i)

gastos=0
valor_gasto=0
while gastos < 1000
    valor_gasto = int(input(“Digite o valor gasto”))
    gastos = gastos + valor_gasto
print(gastos)
```
* https://youtu.be/GUanHEGlje4?si=Yftwbg-0TWIfoR8l
  * Procurar por patterns quando ele vai te ajudar, não só pq aprendeu e quer aplicar sem necessidade.
  * Evitar complexidade ciclomatica (fors dentro de fors, muitos ifs e elses). Separar blocos em funções.
  * Não programamos pro computador, programamos para o próximo dev que for mexer no nosso código.
  * Linters ajudam automatizando boas práticas e dando nota para nosso código.
  * As melhores boas práticas são os que a equipe combinou. Se a equipe não tem boa comunicação, não interessa o check list que coloquemos, nosso código vai ser zuado.
  * Simplicidade e clareza.
  * Métodos e funções menores.
  * Variaveis e métodos claros.
  * Testes para garantir qualidade do código.
  * Evitar enfiar patterns em tudo conté canto sem necessidade.
* Módulos e bibliotecas em Python:
  * Um módulo é um arquivo Python contendo definições e instruções.
  * Conjunto de módulos chamamos de pacotes ou biblioteca.
  * import circulo: importa tudo de dentro da classe, como variaveis e funções.
  * from circulo import area: importa só o método área.
  * O PYTHONPATH é uma lista de diretórios na qual o interpretador Python irá buscar por módulos para importação.
* PyPI:
  * O Python Package Index, abreviado como PyPI é o repositório de software oficial de terceiros para Python.
* Ambientes virtuais:
  * Forma de rodar especificamente a versão de uma biblioteca diferente da que é necessário entre aplicação A e B, para não causar conflitos.
  * Ambiente virtual é uma arvore de diretórios que contenha uma instalação python para uma versão particular do python e pacotes adicionais.
* Python e IA:
  * TensorFlow e Keras: Deep Learning do Google
  * PyTorch: DL do Facebook.
* Bibliotecas mais utilizadas:
  * NumPy: para computação numérica, permite a manipulação de arrays multidimensionais e funções matemáticas de alto desempenho.
  * Pandas: para manipulação e análise de dados, fornece estruturas de dados flexíveis e eficientes para trabalhar com dados tabulares.
  * Matplotlib: para criação de gráficos e visualizações de dados em Python.
  * TensorFlow: framework de aprendizado de máquina de código aberto para desenvolver e treinar modelos de aprendizado profundo.
  * Django: framework web de alto nível que facilita o desenvolvimento rápido e seguro de aplicativos web.
  * Flask: framework web leve e flexível para a criação de aplicativos web em Python.
  * SciPy: biblioteca para computação científica que fornece funcionalidades para otimização, interpolação, processamento de sinais, álgebra linear e muito mais.
  * Scikit-learn: para aprendizado de máquina, fornece algoritmos de classificação, regressão, clustering e pré-processamento de dados.
  * BeautifulSoup: para extração de dados de páginas web, permitindo a raspagem de dados de forma fácil e eficiente.
  * Requests: para fazer requisições HTTP de maneira simples e fácil, muito útil para acessar APIs e baixar conteúdo da web.
  * Pillow: para processamento de imagens, oferece funcionalidades para abrir, manipular e salvar muitos formatos de arquivos de imagem.
  * Asyncio: para programação assíncrona, permite escrever código concorrente usando a estrutura de async/await, facilitando a execução de operações de I/O de forma eficiente.
  * Tkinter: biblioteca padrão do Python para a criação de interfaces gráficas (GUI), permitindo o desenvolvimento de aplicativos desktop com uma variedade de widgets.
* As sugestões que aparecem na plataforma são resultados de análises de hábitos de compras e padrões de busca, realizadas tanto com Python — machine learning e Big Data.
* Ouvir podcast: https://cursos.alura.com.br/extra/hipsterstech/ecossistema-python-hipsters-ponto-tech-387-a9175
* 
