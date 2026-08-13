# Desenvolvimento em Python 

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![Licença](https://img.shields.io/badge/uso-educacional-green)
![Status](https://img.shields.io/badge/status-em%20evolução-blue)

Repositório de estudos da linguagem Python, criado para registrar **exercícios, exemplos comentados e mini-projetos** desenvolvidos ao longo da minha formação em desenvolvimento Python (OneBitCode).

O repositório é organizado em **quatro trilhas de aprendizado** que seguem a progressão natural do curso: dos fundamentos da linguagem, passando pela biblioteca padrão e módulos externos, chegando à Programação Orientada a Objetos e a exercícios aplicados com testes automatizados.

> **Filosofia do repositório:** cada arquivo é pequeno, executável de forma isolada e comentado. A ideia não é construir um único sistema grande, mas ter um **caderno de código vivo** — onde cada conceito pode ser rodado, alterado e observado na prática.

---

## Índice

- [Panorama do escopo](#panorama-do-escopo)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Trilha 1 — Fundamentos da linguagem](#trilha-1--fundamentos-da-linguagem-pythonfundamentos)
- [Trilha 2 — Módulos e biblioteca padrão](#trilha-2--módulos-e-biblioteca-padrão-módulos)
- [Trilha 3 — Programação Orientada a Objetos](#trilha-3--programação-orientada-a-objetos-poo)
- [Trilha 4 — Exercícios aplicados e testes](#trilha-4--exercícios-aplicados-e-testes-exercicios)
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
| 1. Fundamentos | `PythonFundamentos/` | 24 | Sintaxe, tipos, estruturas de dados, controle de fluxo e funções |
| 2. Módulos | `módulos/` | 19 | Biblioteca padrão, módulos próprios e pacotes externos |
| 3. POO | `POO/` | 6 | Classes, instâncias, construtores, métodos e dunder methods |
| 4. Aplicados | `exercicios/` | 4 | Projetos de terminal, documentação técnica e testes unitários |

Aproximadamente **1.600 linhas de código** distribuídas em **53 arquivos Python**.

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
│   └── Exercício_FinalMódulo1.py   # PROJETO: gestão de times e jogadores
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
│   └── iris.json                   # dataset usado por archive.py
│
├── POO/                        # Trilha 3 — orientação a objetos
│   ├── classe.py                   # definição de classe e atributos
│   ├── instancia.py                # criação e uso de instância
│   ├── construtor.py               # __init__ e __str__
│   ├── metodos.py                  # métodos de instância
│   ├── exercicio01.py              # EXERCÍCIO: avaliação e média de filmes
│   └── exercicio02.py              # EXERCÍCIO: classe Produto com desconto
│
├── exercicios/                 # Trilha 4 — exercícios aplicados
│   ├── ex1.py                      # PROJETO: controle de estoque
│   ├── ex2.py                      # PROJETO: jogo da forca
│   ├── ex3.py                      # PROJETO: gestão de notas escolares
│   └── test_notas.py               # testes unitários (unittest) do ex3
│
├── person.txt                  # saída gerada por módulos/archive.py
├── requirements.txt            # dependências do ambiente virtual
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

---

## Trilha 3 — Programação Orientada a Objetos (`POO/`)

Construção incremental do conceito de classe, usando um **catálogo de filmes** como domínio.

A progressão dos arquivos é intencional e deve ser lida nesta ordem:

1. **`classe.py`** — a classe mais simples possível: apenas atributos de classe com valores padrão.
2. **`instancia.py`** — criação do objeto e atribuição de atributos **após** a instanciação, evidenciando o problema que o construtor resolve.
3. **`construtor.py`** — introdução do `__init__` (todos os dados chegam na criação do objeto) e do dunder `__str__`, que define a representação textual do objeto.
4. **`metodos.py`** — comportamento junto aos dados: o método `technical_sheet()` imprime a ficha técnica do filme.

### Exercícios avaliativos

| Arquivo | Desafio | Conceitos aplicados |
| --- | --- | --- |
| `exercicio01.py` | **Avaliação e média de filmes** — registrar notas, contar avaliadores e calcular a média | Atributos de estado (`totalEvaluation`, `evaluators`), métodos que **mutam** o objeto e método derivado (`average`) |
| `exercicio02.py` | **Classe Produto com desconto** — calcular o preço final a partir de um percentual | Construtor, `__str__` e método com parâmetro que **retorna** valor em vez de imprimir |

> A diferença entre `evaluate()` (que altera o estado interno) e `discount()` (que apenas calcula e retorna) é justamente a lição central desta trilha: **objeto guarda estado, método define comportamento**.

---

## Trilha 4 — Exercícios aplicados e testes (`exercicios/`)

Onde os fundamentos viram programas completos. Estes arquivos têm **docstrings, justificativas de decisão de projeto e comentários explicando o "porquê"**, não apenas o "o quê".

### `ex1.py` — Sistema de controle de estoque

Aplicação de terminal com menu em laço `while`.

- Visualizar o estoque atual com preços formatados (`R$ {valor:.2f}`)
- Registrar **entrada** de produto (busca *case-insensitive*)
- Registrar **saída** com **dupla validação**: produto existente e saldo suficiente
- Impede que o estoque atinja valores negativos (estado inválido)

> **Decisão documentada no código:** lista de dicionários em vez de dicionário puro, porque o nome não é um identificador estável e a lista facilita a futura migração para um banco de dados.

### `ex2.py` — Jogo da Forca

Jogo completo em modo texto, com arquitetura em funções puras e docstrings no padrão Google.

- `inicializar_jogo()` monta o dicionário de estado da partida
- `processar_tentativa()` recebe o estado e uma letra e devolve o feedback
- `main()` controla o laço, valida a entrada e exibe uma barra visual de tentativas
- Protegido por `if __name__ == "__main__":`

> **Decisão documentada no código:** `set` para as letras tentadas (unicidade automática e busca em **O(1)**) e `list` para a palavra oculta (preserva a **posição** de cada letra). O arquivo explica por que uma `list` seria O(n) para o histórico de tentativas.

### `ex3.py` — Gestão de notas escolares

- `calcular_media(notas)` — média aritmética, com `raise ValueError` para lista vazia
- `verificar_aprovacao(media, media_minima=7.0)` — parâmetro com valor padrão
- `gerar_relatorio(alunos)` — relatório formatado no terminal

### `test_notas.py` — Testes unitários

Suíte com `unittest` cobrindo o `ex3.py`:

- Casos normais de aprovação e reprovação
- **Caso de erro:** `calcular_media([])` deve levantar `ValueError` (verificado com `assertRaises`)
- **Caso de borda:** aprovação com `media_minima=0`

---

## Projetos em destaque

### Gestão de Times e Jogadores — `PythonFundamentos/Exercício_FinalMódulo1.py`

Projeto de revisão do Módulo 1, que consolida **todos** os fundamentos em um único sistema de terminal. Usa um dicionário de times, onde cada time guarda seu nome e uma lista de jogadores.

Funcionalidades:

- Adicionar e remover times (remoção por índice, com validação)
- Listar times exibindo índice, nome e **quantidade de jogadores**
- Adicionar e remover jogadores de um time específico
- Listar os jogadores de um time
- Menu contínuo com opção de saída

Recursos aplicados: dicionários aninhados, listas, funções auxiliares (`print_teams`, `print_team_players`), `enumerate()`, laço `while`, `if/elif/else` e validação de entrada.

### Jogo da Forca — `exercicios/ex2.py`

O exemplo mais maduro do repositório em termos de organização de código: separação de responsabilidades em funções, estado isolado em dicionário, docstrings completas e escolha de estruturas de dados justificada por complexidade algorítmica.

### Controle de Estoque — `exercicios/ex1.py`

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

### 3. Instalar as dependências

Necessário apenas para os arquivos que usam pacotes externos (`desenho.py`):

```bash
pip install -r requirements.txt
```

> A maior parte do repositório roda **sem nenhuma dependência externa**, usando apenas a biblioteca padrão.

### 4. Executar um arquivo

Cada arquivo é independente e executável isoladamente:

```bash
# Projeto final do módulo 1
python "PythonFundamentos/Exercício_FinalMódulo1.py"

# Jogo da forca
python exercicios/ex2.py

# Exercício de POO
python POO/exercicio01.py

# Relatório de notas (importe e chame gerar_relatorio)
python exercicios/ex3.py
```

> **Atenção ao diretório de trabalho:** alguns arquivos da pasta `módulos/` usam caminhos relativos. Para `archive.py` (que lê `iris.json`) e `1-modulos.py` / `result1.py` (que importam módulos vizinhos), execute a partir da própria pasta:
>
> ```bash
> cd "módulos"
> python archive.py
> ```

---

## Testes automatizados

A suíte de testes do sistema de notas roda a partir da pasta `exercicios/` (o teste importa `ex3` como módulo vizinho):

```bash
cd exercicios
python -m unittest test_notas.py -v
```

Ou, para descobrir todos os testes da pasta:

```bash
cd exercicios
python -m unittest discover -v
```

---

## Observações e avisos importantes

| Arquivo | Observação |
| --- | --- |
| `PythonFundamentos/Exercicios.py` | Usa `winsound`, disponível **somente no Windows**. Grande parte do arquivo está comentada de propósito — são exercícios resolvidos e arquivados. |
| `módulos/exercicio2.py` | Contém comandos reais de **desligamento do computador** (`shutdown /s`). As chamadas estão comentadas e o script termina executando `cancel_shutdown()`. Leia antes de rodar. |
| `módulos/OS.py` | Executa `os.system('ver')` e `os.system('systeminfo')` — comandos específicos do **Windows**. |
| `módulos/interface.py` | Abre uma janela `tkinter`; requer ambiente gráfico. |
| `módulos/desenho.py` | Depende do pacote externo `sketchpy` (instalado via `requirements.txt`). |
| `módulos/archive.py` | Escreve o arquivo `person.txt` no diretório em que for executado. |
| Nomes de arquivo | Alguns arquivos e pastas usam acentos (`módulos/`, `função_lambda.py`, `Exercício_FinalMódulo1.py`). Sempre use **aspas** ao informar esses caminhos no terminal. |

---

## Competências desenvolvidas

Ao percorrer as quatro trilhas, este repositório exercita:

- **Sintaxe e semântica de Python** — tipos, operadores, controle de fluxo e escopo
- **Escolha de estruturas de dados** — saber *quando* usar lista, tupla, set ou dicionário, e por quê (complexidade, mutabilidade, unicidade e ordenação)
- **Decomposição em funções** — parâmetros padrão, `*args`/`**kwargs`, retorno vs. efeito colateral e recursividade
- **Modularização** — criar módulos próprios e separar biblioteca de aplicação
- **Biblioteca padrão** — `math`, `statistics`, `random`, `collections`, `hashlib`, `json`, `re`, `os`, `webbrowser`, `tkinter`
- **Orientação a objetos** — classes, instâncias, construtores, métodos e dunder methods (`__init__`, `__str__`)
- **Tratamento de erros e validação de entrada** — `raise ValueError`, checagens defensivas e mensagens claras ao usuário
- **Testes automatizados** — `unittest`, casos normais, de erro e de borda
- **Documentação de código** — docstrings no padrão Google e comentários que explicam decisões de projeto
- **Aplicações de terminal** — menus em laço, leitura de entrada, formatação de saída e encerramento controlado

---

## Objetivo

Repositório de **finalidade educacional**, que acompanha e documenta minha evolução no aprendizado de Python — dos primeiros `print()` até projetos estruturados com testes automatizados.

## Autor

Desenvolvido por [Davi Morais](https://github.com/DaviMoraisdev).
