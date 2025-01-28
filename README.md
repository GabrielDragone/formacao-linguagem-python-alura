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

---

### Python: Crie a sua primeira aplicação:

#### 01. Manipulação de Strings:

* 03 - Primeiro programa:
  * A ideia é termos um aplicativo de comida/restaurante.
  * Será desenvolvimento backend.
  * Criamos um arquivo app.py e pra rodar digitamos python e o nome do arquivo.
* 04 - Boas práticas:
  * Python utiliza o snake case / underscore case para variáveis, funções e métodos.
  * Classes ficam no PascalCase.
* 05 - Interpolação de String:
  * Python aceita aspas duplas e simples.
  * O ideal é escolher um padrão pro projeto e mante-lo sempre igual.
  * Também podemos usar as aspas duplas três vezes, para manter as quebras de linhas.
  * Usado https://fsymbols.com/ para pegar textos diferentes.
  * Para usar interpolação de strings, basta colocar um f antes da string e deixar as variáveis entre chaves.
* 06 - Para saber mais: The Zen of Python:
```
  Bonito é melhor que feio.\
  Explícito é melhor que implícito.\
  Simples é melhor que complexo.\
  Complexo é melhor que complicado.\
  Plano é melhor que aninhado.\
  Esparso é melhor que denso.\
  Legibilidade conta.\
  Casos especiais não são especiais o bastante para quebrar as regras.\
  Embora praticidade vença a pureza.\
  Erros nunca devem passar silenciosamente.\
  A menos que sejam explicitamente silenciados.\
  Diante da ambiguidade, recuse a tentação de adivinhar.\
  Deveria haver uma — e preferencialmente só uma — maneira óbvia de fazer algo.\
  Embora essa maneira possa não ser óbvia a princípio a menos que você seja holandês.\
  Agora é melhor que nunca.\
  Embora nunca seja frequentemente melhor que agora mesmo.\
  Se a implementação é difícil de explicar, é uma má ideia.\
  Se a implementação é fácil de explicar, pode ser uma boa ideia.\
  Namespaces são uma grande ideia — vamos fazer mais dessas!\
```
* 07 - Hora da prática: a função print():
  * Criado [print_example.py](python-crie-sua-primeira-aplicacao/print_example.py) com exemplos.

#### 02. Módulos e funções:

* 03 - Tipo int e bool:
  * Por padrão quando usamos o input, o python atribui a variavel como string.
  * Temos que tratar essa variavel alterando para int.
* 04 - Funções e import:
  * Escrever funções no padrão snake_case.
  * Para importar algo `import os`.
  * Função bloco de código que vai executar uma ação (ideal) no momento que for chamada.
* 05 - Aprofundando em funções:
  * Para definir o arquivo principal do programa, criar a função main.
  * Quando pedimos pra um programa em python ser executado, o interpretador criar uma variavel chamada name.
  * E se o name for main, significa que esse código não será importado por outros scripts do código python.
  * Separadas as funções de exibir nome do programa, menu e escolha de opções.
  * Dentro do main definido todos os passos pro programa executar.
* 06 - Para saber mais: instruções match:
  * Uma forma mais elegante e simplificada de trabalhar com opções.
  * Vantagens do Match:
    * Lidar com condições complexas e múltiplos padrões de maneira mais intuitiva.
    * Sintaxe concisa melhora a legibilidade do código, especialmente em casos complexos.
    * Permite desestruturação direta, evitando repetição excessiva de variáveis.
    * Adiciona expressividade ao código, especialmente em situações de correspondência de padrões.	
  * Vantagens do If:
    * Implementação clássica e amplamente conhecida.
    * Amplamente suportada em todas as versões do Python.
    * Estrutura simples e direta para lógica condicional básica.
    * Pode ser mais intuitiva para devs familiarizados com estruturas de controle convencionais.
* 09 - Hora da prática: condicionais:
  * Realizado no arquivo: [exercicios_02_09.py](python-crie-sua-primeira-aplicacao/exercicios_02_09.py)

#### 03. Lista, laços e exceções:

* 02 - Try except:
  * Usar try: except: equivalente ao try catch.
  * Exemplos no app.py.
* 03 - Listas:
  * Implementação de função para cadastro de restaurantes.
  * Criada variavel global de lista [].
  * Para adicionar novos itens na lista usar append.
* 04 - Tuplas vs Listas:
  * Tuplas e listas são estruturas de dados que permitem armazenar elementos de maneira ordenada e sequencial.
  * Sintaxe:
    * ``lista = [1,’olá mundo’,True,9.7]``
    * ``tupla = (1,’olá mundo’,True,9.7)``
  * Listas são estruturas mutáveis, ou seja, podemos modificar, adicionar, remover através de append, remove, pop e insert. Menos eficiente especialmente quando se trata de manipulação de grandes conjuntos de dados.
  * Tuplas são imutáveis, uma vez declarada, não podem ser alteradas e devido à isso, tem um desempenho melhor para operações.
* 05 - Laços de repetição for:
  * Usar da seguinte forma: ```for restaurante in restaurantes:```
* 06 - While:
  * [while_example.py](python-crie-sua-primeira-aplicacao/for_while_example.py)
  * O for é utilizado quando se conhece previamente o número de iterações que devem ser realizadas.
    * Ideal em casos de elementos em sequências como listas, tuplas, strings ou ranges.
  * Python fornece for e while como estruturas de repetição para execução de blocos.
  * O while será usado quando não se conhece previamente o número de iterações que devem ser realizadas, mas ainda sim precisa de uma condição específica pra manter o bloco de código em repetição.
  * A escolha entre um ou outro vai depender da natureza específica do problema que estamos resolvendo.
* 07 - Refatorando o código:
  * Refatorando trechos repetidos.