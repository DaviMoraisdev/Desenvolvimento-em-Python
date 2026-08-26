# Desenvolvimento em Python 

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![Licença](https://img.shields.io/badge/uso-educacional-green)
![Status](https://img.shields.io/badge/status-em%20evolução-blue)

Repositório de estudos da linguagem Python, criado para registrar **exercícios, exemplos comentados e mini-projetos** desenvolvidos ao longo da minha formação em desenvolvimento Python (OneBitCode).

O repositório é organizado em **quatro trilhas de aprendizado** que seguem a progressão natural do curso: dos fundamentos da linguagem, passando pela biblioteca padrão e módulos externos, chegando à Programação Orientada a Objetos e ao tratamento de erros com testes automatizados.

> **Filosofia do repositório:** cada arquivo é pequeno, executável de forma isolada e comentado. A ideia não é construir um único sistema grande, mas ter um **caderno de código vivo** — onde cada conceito pode ser rodado, alterado e observado na prática.

---

## Índice

- [Panorama do escopo](#panorama-do-escopo)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Trilha 1 — Fundamentos da linguagem](#trilha-1--fundamentos-da-linguagem-pythonfundamentos)
- [Trilha 2 — Módulos e biblioteca padrão](#trilha-2--módulos-e-biblioteca-padrão-módulos)
- [Trilha 3 — Programação Orientada a Objetos](#trilha-3--programação-orientada-a-objetos-poo)
- [Trilha 4 — Tratamento de erros e testes](#trilha-4--tratamento-de-erros-e-testes-tratamento-de-erros)
- [Projetos em destaque](#projetos-em-destaque)
- [Como executar](#como-executar)
- [Testes automatizados](#testes-automatizados)
- [Observações e avisos importantes](#observações-e-avisos-importantes)
- [Competências desenvolvidas](#competências-desenvolvidas)
- [Autor](#autor)

---

## Panorama do escopo

| Trilha | Pasta | Arquivos | Foco de aprendizado |
| --- | --- | --- | --- |
| 1. Fundamentos | `PythonFundamentos/` | 34 | Sintaxe, tipos, estruturas de dados, controle de fluxo, funções e HOF |
| 2. Módulos | `módulos/` | 23 | Biblioteca padrão, módulos próprios, pacotes externos e projetos de terminal |
| 3. POO | `POO/` | 25 | Classes, herança, polimorfismo, encapsulamento, decorators e composição |
| 4. Erros e testes | `tratamento de erros/` | 4 | `try/except`, `raise`, exceções personalizadas e testes com `pytest` |

Aproximadamente **2.600 linhas de código** distribuídas em **86 arquivos Python**.

---

## Estrutura do repositório

```text
Curso OBC -Python/
├── PythonFundamentos/          # Trilha 1 — fundamentos da linguagem
│   ├── tipos.py                    # tipos primitivos e type()
│   ├── input.py                    # entrada de dados e casting
│   ├── concatena.py                # saída formatada (3 alternativas)
│   ├── Operadores.py               # aritméticos, comparação e lógicos
│   ├── Strings.py                  # strings, multilinhas e métodos
│   ├── slice.py                    # fatiamento [início:fim:passo]
│   ├── if_else.py                  # condicional simples
│   ├── elif.py                     # calculadora com if/elif/else
│   ├── for.py                      # laço for, break e continue
│   ├── while.py                    # laço while e média de avaliações
│   ├── listas.py                   # métodos de lista
│   ├── tuplas.py                   # tuplas (imutabilidade)
│   ├── set.py                      # conjuntos e operações
│   ├── dicionarios.py              # dicionários (CRUD de chaves)
│   ├── DicionariosAninhados.py     # dicionários aninhados + pprint
│   ├── list_comprehension.py       # list comprehension com filtro
│   ├── funcao.py                   # funções, parâmetros e retorno
│   ├── args.py                     # *args e **kwargs
│   ├── função_lambda.py            # funções anônimas
│   ├── funcao_recursivas.py        # recursividade (fatorial e somatório)
│   ├── Exercicio.py                # exercícios de entrada e média
│   ├── Exercicio5.py               # contagem de maiúsculas/minúsculas
│   ├── Exercicios.py               # exercícios variados + winsound
│   ├── Exercício_FinalMódulo1.py   # PROJETO: gestão de times e jogadores
│   │
│   └── Base/                   # revisão dos fundamentos com type hints
│       ├── função.py               # definição de função e retorno
│       ├── aegs_kwargs.py          # *args, **kwargs, spread e mutabilidade
│       ├── funcoes_recursivas.py   # fatorial recursivo
│       ├── lambda_e_hof.py         # lambda, map, sort(key=) e Callable
│       ├── exercicios.py           # antecessor/sucessor, média e strings
│       ├── exercicio2.py           # lista de pedidos (pop e acesso por índice)
│       ├── exercicio3.py           # contagem regressiva, tabuada e filtro
│       ├── exercicio4.py           # funções puras, filtros e desconto
│       ├── exercicio5.py           # Counter + random, regex e json
│       └── exercicio6.py           # classes: Filme, Biblioteca e ListaTarefas
│
├── módulos/                    # Trilha 2 — módulos e biblioteca padrão
│   ├── calc.py                     # módulo próprio (sum, sub, mult, div)
│   ├── 1-modulos.py                # import de módulo próprio
│   ├── 2-modules.py                # help('modules')
│   ├── math.py                     # módulo math
│   ├── statistic.py                # statistics (média, mediana, moda, desvio)
│   ├── aleatorio.py                # random (choice, randint, sample)
│   ├── coleções.py                 # collections (Counter, namedtuple, deque)
│   ├── cripto.py                   # hashlib (SHA-256 e MD5)
│   ├── archive.py                  # json (loads, dumps, load, dump)
│   ├── text.py                     # re — expressões regulares
│   ├── OS.py                       # os — sistema operacional
│   ├── webpage.py                  # webbrowser — abrir URLs
│   ├── interface.py                # tkinter — interface gráfica
│   ├── desenho.py                  # sketchpy — desenho por código
│   ├── exercicio1.py               # módulo de tratamento de strings
│   ├── result1.py                  # consumo do módulo exercicio1
│   ├── exercicio2.py               # agendamento de desligamento (os)
│   ├── exercicio3.py               # validação de caracteres com regex
│   ├── exercicio4.py               # jogo: adivinhe o número
│   ├── iris.json                   # dataset usado por archive.py
│   │
│   └── exercicios/             # projetos aplicados da trilha
│       ├── ex1.py                  # PROJETO: controle de estoque
│       ├── ex2.py                  # PROJETO: jogo da forca
│       ├── ex3.py                  # PROJETO: gestão de notas escolares
│       └── test_notas.py           # testes unitários (unittest) do ex3
│
├── POO/                        # Trilha 3 — orientação a objetos
│   ├── classe.py                   # definição de classe e atributos
│   ├── instancia.py                # criação e uso de instância
│   ├── construtor.py               # __init__ e __str__
│   ├── metodos.py                  # métodos de instância
│   ├── class_variable.py           # atributo de classe vs. de instância
│   ├── class_method.py             # @classmethod como construtor alternativo
│   ├── static_method.py            # @staticmethod (sem self/cls)
│   ├── encapsulamento.py           # atributo privado (__salary) e name mangling
│   ├── getter_setter.py            # acesso controlado por métodos
│   ├── property.py                 # @property e @setter com validação
│   ├── heranca.py                  # herança simples (Animal → Horse/Lion)
│   ├── super.py                    # super().__init__() na subclasse
│   ├── polimorfismo.py             # sobrescrita de método (discount)
│   ├── composição.py               # objeto que contém outros objetos (Zoo)
│   ├── decorator.py                # módulo com três decorators
│   ├── decorators.py               # aplicação dos decorators com @
│   ├── teste_re.py                 # regex com grupos nomeados (base do class_method)
│   ├── exercicio01.py              # EXERCÍCIO: avaliação e média de filmes
│   ├── exercicio02.py              # EXERCÍCIO: classe Produto com desconto
│   ├── exercicio03.py              # EXERCÍCIO: classe Viagem (enunciado + classe)
│   ├── exercicio03exec.py          # execução do cadastro de viagem
│   ├── enum_exerciciofinal.py      # enunciado do projeto final da trilha
│   ├── contato.py                  # classe Contact (modelo)
│   ├── contato_agenda.py           # classe ContactBook (CRUD de contatos)
│   ├── exercicio_final.py          # PROJETO: agenda de contatos (menu)
│   └── Img1.jpg                    # imagem usada nos estudos
│
├── tratamento de erros/        # Trilha 4 — erros e testes
│   ├── try_except.py               # try/except/else/finally e múltiplos excepts
│   ├── raise.py                    # raise, exceções personalizadas e atributos
│   ├── testes.py                   # funções sob teste (dobro, raiz_quadrada)
│   └── tests/
│       └── test_calc.py            # testes com pytest (assert puro)
│
├── .gitignore
└── README.md
```

---

## Trilha 1 — Fundamentos da linguagem (`PythonFundamentos/`)

Base da linguagem, construída de forma incremental. O tema condutor dos exemplos é um **catálogo de jogos**, o que dá continuidade narrativa aos conceitos.

### Conteúdos praticados

| Tema | Arquivo | O que se aprende |
| --- | --- | --- |
| Tipos de dados | `tipos.py` | `str`, `int`, `float`, `bool` e inspeção com `type()` |
| Entrada de dados | `input.py` | Leitura via `input()` e conversão explícita (`int()`, `float()`) |
| Saída formatada | `concatena.py` | Três formas de exibir dados: vírgulas, concatenação e **f-strings** |
| Operadores | `Operadores.py` | Aritméticos (`%`, `**`), comparação e o resultado booleano de cada um |
| Strings | `Strings.py` | Case sensitivity, strings multilinhas e operações de texto |
| Fatiamento | `slice.py` | `string[início:fim:passo]`, índices negativos e inversão |
| Condicionais | `if_else.py`, `elif.py` | Decisão simples e encadeada — inclui uma calculadora de 4 operações |
| Repetição | `for.py`, `while.py` | `range()`, `break`, `continue` e laço com condição de parada por sentinela (`-1`) |
| Listas | `listas.py` | `len`, `index`, `append`, `sort`, `copy`, `remove`, `clear` |
| Tuplas | `tuplas.py` | Imutabilidade e acesso por índice/fatia |
| Conjuntos | `set.py` | Unicidade automática, `update`, `remove` e o caso `True == 1` |
| Dicionários | `dicionarios.py` | `values()`, `items()`, inserção e atualização de chaves |
| Dicionários aninhados | `DicionariosAninhados.py` | Estruturas em profundidade e leitura formatada com `pprint` |
| List comprehension | `list_comprehension.py` | Compactar `for` + `if` em uma única expressão |
| Funções | `funcao.py` | Definição, chamada, parâmetros e `return` vs `print` |
| Args dinâmicos | `args.py` | `*args` (tupla) e `**kwargs` (dicionário) |
| Lambda | `função_lambda.py` | Funções anônimas de uma linha (potência, paridade, inversão) |
| Recursividade | `funcao_recursivas.py` | Fatorial e somatório com caso base e chamada recursiva |

### Subpasta `Base/` — revisão com type hints

Segunda passada pelos fundamentos, agora escrevendo o código com **anotações de tipo** (`def somar(a: int, b: int) -> int`) e resolvendo exercícios maiores.

| Arquivo | O que traz de novo |
| --- | --- |
| `função.py` | Retorno de função e por que código depois do `return` nunca executa |
| `aegs_kwargs.py` | Assinatura completa `(a, b, *args, chave1=10, **kwargs)`, operador spread (`[*lista, item]`) e **mutabilidade de listas passadas como argumento** |
| `funcoes_recursivas.py` | Fatorial recursivo isolado |
| `lambda_e_hof.py` | **Higher-order functions**: `map`, `sort(key=lambda ...)` e função recebida por parâmetro tipada com `Callable[[int, int], int]` |
| `exercicios.py` | Antecessor/sucessor, média de três notas e manipulação de strings |
| `exercicio2.py` | Lista de dicionários de pedidos: `pop()` com índice negativo e acesso por índice |
| `exercicio3.py` | Contagem regressiva com `range(10, -1, -1)`, tabuada e filtro de produtos por preço |
| `exercicio4.py` | Decomposição em funções puras (`eh_par`, `filtra_pares`) e parâmetro com valor padrão |
| `exercicio5.py` | Integração de três módulos: `Counter` + `random`, regex `\b[A-Z]{2}\d{4}\b` e `json.loads` |
| `exercicio6.py` | Primeiras classes antes da Trilha 3: `Filme`, `Biblioteca` e `ListaTarefas` |

---

## Trilha 2 — Módulos e biblioteca padrão (`módulos/`)

Como **reaproveitar código**: criando módulos próprios e consumindo a biblioteca padrão e pacotes externos.

### Módulos próprios

- **`calc.py` + `1-modulos.py`** — criação de um módulo de calculadora e as duas formas de importar: `import calc` e `from calc import div`.
- **`exercicio1.py` + `result1.py`** — módulo de tratamento de strings (inverter, caracteres de índice par e ímpar) consumido por um script separado. Demonstra a separação entre **biblioteca** e **aplicação**.

### Biblioteca padrão

| Módulo | Arquivo | Recursos explorados |
| --- | --- | --- |
| `math` | `math.py` | `pi`, `e`, `ceil`, `floor`, `factorial`, `pow`, `sqrt`, `gcd`, `log` |
| `statistics` | `statistic.py` | `mean`, `median`, `mode` e `stdev` (com nota sobre dispersão) |
| `random` | `aleatorio.py` | `choice`, `randint` e `sample` sobre listas e strings |
| `collections` | `coleções.py` | `Counter`, `namedtuple`, `deque` e ordenação com `itemgetter` |
| `hashlib` | `cripto.py` | Algoritmos disponíveis, `sha256()` e `md5()` com `hexdigest()` |
| `json` | `archive.py` | `loads`/`dumps` (string ↔ dict), `indent`, `sort_keys` e leitura/escrita em arquivo |
| `re` | `text.py`, `exercicio3.py` | `search`, `findall`, `match`, `compile`, âncoras `^`/`$` e classes `[a-m]` |
| `os` | `OS.py`, `exercicio2.py` | `getcwd`, `listdir` e execução de comandos do sistema |
| `webbrowser` | `webpage.py` | `open_new_tab()` dentro de um menu interativo |
| `tkinter` | `interface.py` | Janela, `Frame`, `Label`, `Entry`, `Button` e callback de evento |

### Pacotes externos

- **`desenho.py`** — usa `sketchpy` para gerar um desenho a partir de traços vetoriais.

### Exercícios da trilha

- **`exercicio2.py`** — funções para agendar/cancelar o desligamento do computador via `os.system("shutdown")`.
- **`exercicio3.py`** — valida com regex se uma string contém **apenas** `a-z`, `A-Z` e `0-9`.
- **`exercicio4.py`** — jogo "adivinhe o número" com menu em laço e sorteio via `random.randint`.

### Projetos aplicados (`módulos/exercicios/`)

Onde os fundamentos viram programas completos. Estes arquivos têm **docstrings, justificativas de decisão de projeto e comentários explicando o "porquê"**, não apenas o "o quê".

#### `ex1.py` — Sistema de controle de estoque

Aplicação de terminal com menu em laço `while`.

- Visualizar o estoque atual com preços formatados (`R$ {valor:.2f}`)
- Registrar **entrada** de produto (busca *case-insensitive*)
- Registrar **saída** com **dupla validação**: produto existente e saldo suficiente
- Impede que o estoque atinja valores negativos (estado inválido)

> **Decisão documentada no código:** lista de dicionários em vez de dicionário puro, porque o nome não é um identificador estável e a lista facilita a futura migração para um banco de dados.

#### `ex2.py` — Jogo da Forca

Jogo completo em modo texto, com arquitetura em funções puras e docstrings no padrão Google.

- `inicializar_jogo()` monta o dicionário de estado da partida
- `processar_tentativa()` recebe o estado e uma letra e devolve o feedback
- `main()` controla o laço, valida a entrada e exibe uma barra visual de tentativas
- Protegido por `if __name__ == "__main__":`

> **Decisão documentada no código:** `set` para as letras tentadas (unicidade automática e busca em **O(1)**) e `list` para a palavra oculta (preserva a **posição** de cada letra). O arquivo explica por que uma `list` seria O(n) para o histórico de tentativas.

#### `ex3.py` — Gestão de notas escolares

- `calcular_media(notas)` — média aritmética, com `raise ValueError` para lista vazia
- `verificar_aprovacao(media, media_minima=7.0)` — parâmetro com valor padrão
- `gerar_relatorio(alunos)` — relatório formatado no terminal

#### `test_notas.py` — Testes unitários com `unittest`

- Casos normais de aprovação e reprovação
- **Caso de erro:** `calcular_media([])` deve levantar `ValueError` (verificado com `assertRaises`)
- **Caso de borda:** aprovação com `media_minima=0`

---

## Trilha 3 — Programação Orientada a Objetos (`POO/`)

A trilha mais extensa do repositório. Começa no conceito mínimo de classe e chega aos quatro pilares da OO, decorators e composição, sempre com exemplos pequenos e executáveis.

### 1. Do zero à classe completa

A progressão dos arquivos é intencional e deve ser lida nesta ordem:

1. **`classe.py`** — a classe mais simples possível: apenas atributos de classe com valores padrão.
2. **`instancia.py`** — criação do objeto e atribuição de atributos **após** a instanciação, evidenciando o problema que o construtor resolve.
3. **`construtor.py`** — introdução do `__init__` (todos os dados chegam na criação do objeto) e do dunder `__str__`, que define a representação textual do objeto.
4. **`metodos.py`** — comportamento junto aos dados: o método `technical_sheet()` imprime a ficha técnica do filme.
5. **`class_variable.py`** — a diferença entre atributo **de classe** (`Movie.platform`, compartilhado por todas as instâncias) e atributo **de instância** (`self.name`).

### 2. Tipos de método

| Arquivo | Decorator | Recebe | Uso demonstrado |
| --- | --- | --- | --- |
| `metodos.py` | — | `self` | Comportamento ligado a **uma instância** |
| `class_method.py` | `@classmethod` | `cls` | **Construtor alternativo**: `Console.from_text(...)` cria o objeto a partir de uma frase, usando regex com grupos nomeados |
| `static_method.py` | `@staticmethod` | nada | Função utilitária que vive na classe por organização (`Language.courses_trail(trail)`) |

> `teste_re.py` é o rascunho da regex usada em `class_method.py`: `re.fullmatch` com grupos nomeados `(?P<name>\w+)` e `raise ValueError` quando o texto não casa com o padrão.

### 3. Encapsulamento

| Arquivo | Conceito |
| --- | --- |
| `encapsulamento.py` | Atributo privado `self.__salary` e **name mangling** — `Davi.__salary = 44000` cria um atributo novo em vez de alterar o original |
| `getter_setter.py` | Acesso controlado ao atributo privado via `get_salary()` / `set_salary()` |
| `property.py` | A forma *pythônica*: `@property` + `@name.setter` com validação (`raise TypeError` se o nome não for `str`) |

### 4. Herança, polimorfismo e composição

| Arquivo | Conceito | Exemplo |
| --- | --- | --- |
| `heranca.py` | Herança simples | `Animal` → `Horse` e `Lion`, cada uma com atributos e métodos próprios |
| `super.py` | `super().__init__()` | `Smartphone` reaproveita o construtor de `Phone` e acrescenta `ram`, `internal_memory` e `back_camera` |
| `polimorfismo.py` | Sobrescrita de método | `Phone.discount()` devolve 10% e `Smartphone.discount()` devolve 15% — mesma chamada, comportamento diferente |
| `composição.py` | "Tem um" em vez de "é um" | `Zoo` guarda instâncias de `Fish` e `Parrots` e conta os animais por categoria |

### 5. Decorators

- **`decorator.py`** — define três decorators: `my_decorator` (executa código antes e depois), `uppercase_decorator` e `split_string` (transformam o retorno da função).
- **`decorators.py`** — aplica os três com a sintaxe `@`, mostrando que decorar é apenas envolver a função original em um `wrapper`.

### Exercícios avaliativos

| Arquivo | Desafio | Conceitos aplicados |
| --- | --- | --- |
| `exercicio01.py` | **Avaliação e média de filmes** — registrar notas, contar avaliadores e calcular a média | Atributos de estado (`totalEvaluation`, `evaluators`), métodos que **mutam** o objeto e método derivado (`average`) |
| `exercicio02.py` | **Classe Produto com desconto** — calcular o preço final a partir de um percentual | Construtor, `__str__` e método com parâmetro que **retorna** valor em vez de imprimir |
| `exercicio03.py` + `exercicio03exec.py` | **Cadastro de viagem** — escolher um destino entre instâncias já criadas | Separação entre **arquivo de classe** e **arquivo de execução**, import entre módulos vizinhos |
| `enum_exerciciofinal.py` + `contato.py` + `contato_agenda.py` + `exercicio_final.py` | **Agenda de contatos** (projeto final da trilha) | Enunciado, modelo, repositório e aplicação em quatro arquivos separados |

> A diferença entre `evaluate()` (que altera o estado interno) e `discount()` (que apenas calcula e retorna) é justamente a lição central desta trilha: **objeto guarda estado, método define comportamento**.

---

## Trilha 4 — Tratamento de erros e testes (`tratamento de erros/`)

Trilha mais recente do repositório. Sai do "fazer funcionar" para o **"falhar de forma controlada e provar que funciona"**.

### `try_except.py` — capturar e tratar

- Bloco completo `try` / `except` / `else` / `finally`, com a ordem de execução visível na saída
- **Múltiplos `except`** para exceções diferentes (`IndexError` e `ValueError`) no mesmo bloco
- `except ... as error` para acessar a mensagem original da exceção
- `converter_int(valor)` — função que trata `ValueError` (texto não numérico) e `TypeError` (`None`) e devolve `None` em vez de quebrar

> O `except Exception` genérico está comentado de propósito: capturar tudo esconde bugs. A trilha defende **capturar a exceção específica**.

### `raise.py` — levantar e personalizar

Progressão em três níveis:

1. **`raise` com exceção nativa** — `definir_idade()` recusa idade negativa ou acima de 140 com `ValueError`.
2. **Exceção personalizada com estado** — `SaldoInsuficiente(Exception)` guarda `saldo_atual` e `valor_solicitado` como atributos e monta a mensagem no `super().__init__()`. Usada por `ContaBancaria.sacar()`.
3. **Exceção com código de erro** — `EmailInvalidoError` carrega `email`, `motivo` e `codigo_erro`, permitindo que o `except` **decida o que fazer com base no código** (`if e.codigo_erro == "EMAIL_VAZIO"`), em vez de comparar strings de mensagem.

> A lição da trilha: uma exceção personalizada não é só um nome diferente — é um **objeto que transporta o contexto do erro** até quem vai tratá-lo.

### `testes.py` + `tests/test_calc.py` — testes com `pytest`

- `testes.py` expõe `dobro(numero)` (com `raise TypeError` para tipo inválido) e `raiz_quadrada(numero)`, protegidas por `if __name__ == "__main__":`
- `tests/test_calc.py` testa as duas funções com **`assert` puro** — sem classe e sem `self.assertEqual`, que é a diferença prática entre `pytest` e o `unittest` usado na Trilha 2
- O teste ajusta o `sys.path` com `pathlib.Path(__file__).resolve().parent.parent` para importar o módulo da pasta acima, sem precisar de `__init__.py`

---

## Projetos em destaque

### Agenda de Contatos — `POO/exercicio_final.py`

Projeto final da trilha de POO e o exemplo mais bem separado do repositório: **quatro arquivos, quatro responsabilidades**.

- `enum_exerciciofinal.py` — o enunciado do desafio
- `contato.py` — a classe `Contact` (apenas o modelo de dados e seu `__str__`)
- `contato_agenda.py` — a classe `ContactBook`, que **contém** uma lista de contatos e oferece adicionar, remover, listar e buscar
- `exercicio_final.py` — a aplicação: menu em laço `while` que instancia as duas classes e chama os métodos

Destaque para `search_contact()`, que faz a busca *case-insensitive* e **retorna o objeto encontrado** — permitindo que a opção "remover" reaproveite a busca em vez de reimplementá-la.

### Gestão de Times e Jogadores — `PythonFundamentos/Exercício_FinalMódulo1.py`

Projeto de revisão do Módulo 1, que consolida **todos** os fundamentos em um único sistema de terminal. Usa um dicionário de times, onde cada time guarda seu nome e uma lista de jogadores.

Funcionalidades:

- Adicionar e remover times (remoção por índice, com validação)
- Listar times exibindo índice, nome e **quantidade de jogadores**
- Adicionar e remover jogadores de um time específico
- Listar os jogadores de um time
- Menu contínuo com opção de saída

Recursos aplicados: dicionários aninhados, listas, funções auxiliares (`print_teams`, `print_team_players`), `enumerate()`, laço `while`, `if/elif/else` e validação de entrada.

### Jogo da Forca — `módulos/exercicios/ex2.py`

O exemplo mais maduro do repositório em termos de organização de código: separação de responsabilidades em funções, estado isolado em dicionário, docstrings completas e escolha de estruturas de dados justificada por complexidade algorítmica.

### Controle de Estoque — `módulos/exercicios/ex1.py`

Melhor exemplo de **validação defensiva**: nenhuma operação de saída é aplicada antes de confirmar que o produto existe e que há saldo suficiente.

---

## Como executar

### Pré-requisitos

- **Python 3.10 ou superior** (o ambiente do repositório usa Python **3.14**)
- Git

### 1. Clonar o repositório

```bash
git clone https://github.com/DaviMoraisdev/Desenvolvimento-em-Python.git
cd Desenvolvimento-em-Python
```

### 2. Criar e ativar o ambiente virtual

```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências (opcional)

A maior parte do repositório roda **sem nenhuma dependência externa**, usando apenas a biblioteca padrão. Só dois pontos precisam de instalação:

```bash
pip install pytest      # testes da Trilha 4
pip install sketchpy    # apenas para módulos/desenho.py
```

### 4. Executar um arquivo

Cada arquivo é independente e executável isoladamente:

```bash
# Projeto final do módulo 1
python "PythonFundamentos/Exercício_FinalMódulo1.py"

# Jogo da forca
python "módulos/exercicios/ex2.py"

# Exercício de POO
python POO/exercicio01.py

# Tratamento de erros
python "tratamento de erros/raise.py"
```

> **Atenção ao diretório de trabalho:** vários arquivos importam módulos vizinhos ou leem arquivos por caminho relativo. Nesses casos, execute a partir da própria pasta:
>
> ```bash
> cd "módulos"
> python archive.py          # lê iris.json e escreve person.txt
>
> cd POO
> python exercicio_final.py  # importa contato.py e contato_agenda.py
> python exercicio03exec.py  # importa exercicio03.py
> ```

---

## Testes automatizados

O repositório usa **dois frameworks**, um por trilha — de propósito, para comparar as duas abordagens.

### `unittest` — Trilha 2 (`módulos/exercicios/test_notas.py`)

O arquivo importa `módulos.exercicios.ex3` pelo caminho completo, então rode **a partir da raiz do repositório**:

```bash
python -m unittest módulos.exercicios.test_notas -v
```

### `pytest` — Trilha 4 (`tratamento de erros/tests/test_calc.py`)

O teste ajusta o `sys.path` sozinho, então basta apontar para a pasta:

```bash
pip install pytest
python -m pytest "tratamento de erros/tests" -v
```

---

## Observações e avisos importantes

| Arquivo | Observação |
| --- | --- |
| `PythonFundamentos/Exercicios.py` | Usa `winsound`, disponível **somente no Windows**. Grande parte do arquivo está comentada de propósito — são exercícios resolvidos e arquivados. |
| `PythonFundamentos/Base/` | Exercícios de treino em rascunho: alguns arquivos contêm erros propositais ou não corrigidos (chaves com e sem acento, `preco`/`preço`) — servem como registro do processo, não como referência. |
| `módulos/exercicio2.py` | Contém comandos reais de **desligamento do computador** (`shutdown /s`). As chamadas estão comentadas e o script termina executando `cancel_shutdown()`. Leia antes de rodar. |
| `módulos/OS.py` | Executa `os.system('ver')` e `os.system('systeminfo')` — comandos específicos do **Windows**. |
| `módulos/interface.py` | Abre uma janela `tkinter`; requer ambiente gráfico. |
| `módulos/desenho.py` | Depende do pacote externo `sketchpy` (`pip install sketchpy`). |
| `módulos/archive.py` | Escreve o arquivo `person.txt` no diretório em que for executado. |
| `POO/decorators.py` | Usa import relativo (`from .decorator import ...`), então **não roda como script solto**. Execute como módulo a partir da raiz: `python -m POO.decorators`. |
| `POO/exercicio03exec.py`, `POO/exercicio_final.py` | Importam módulos vizinhos — execute de dentro da pasta `POO/`. |
| Nomes de arquivo | Vários arquivos e pastas usam acentos e espaços (`módulos/`, `tratamento de erros/`, `função_lambda.py`, `Exercício_FinalMódulo1.py`). Sempre use **aspas** ao informar esses caminhos no terminal. |

---

## Competências desenvolvidas

Ao percorrer as quatro trilhas, este repositório exercita:

- **Sintaxe e semântica de Python** — tipos, operadores, controle de fluxo e escopo
- **Escolha de estruturas de dados** — saber *quando* usar lista, tupla, set ou dicionário, e por quê (complexidade, mutabilidade, unicidade e ordenação)
- **Decomposição em funções** — parâmetros padrão, `*args`/`**kwargs`, retorno vs. efeito colateral e recursividade
- **Type hints e higher-order functions** — anotações de tipo, `Callable`, `map` e funções recebidas como argumento
- **Modularização** — criar módulos próprios e separar biblioteca de aplicação
- **Biblioteca padrão** — `math`, `statistics`, `random`, `collections`, `hashlib`, `json`, `re`, `os`, `webbrowser`, `tkinter`
- **Orientação a objetos** — os quatro pilares (abstração, encapsulamento, herança e polimorfismo), composição, `@property`, `@classmethod`, `@staticmethod` e dunder methods
- **Decorators** — funções que recebem e devolvem funções, e a sintaxe `@`
- **Tratamento de erros** — `try/except/else/finally`, `raise`, exceções personalizadas com estado e código de erro
- **Testes automatizados** — `unittest` e `pytest`, casos normais, de erro e de borda
- **Documentação de código** — docstrings no padrão Google e comentários que explicam decisões de projeto
- **Aplicações de terminal** — menus em laço, leitura de entrada, formatação de saída e encerramento controlado

---

## Objetivo

Repositório de **finalidade educacional**, que acompanha e documenta minha evolução no aprendizado de Python — dos primeiros `print()` até projetos estruturados com testes automatizados.

## Autor

Desenvolvido por [Davi Morais](https://github.com/DaviMoraisdev).
