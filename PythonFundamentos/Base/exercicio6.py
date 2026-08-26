class Filme:    
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.avaliacao = 0
        self.total_avaliadores = 0

    def exibir_infos(self):
        print(f"Título {self.titulo}")
        print(f"Diretor: {self.diretor}")
        print(f"Ano: {self.ano}")
        print(f"Avaliação: {self.avaliacao}")

    def avaliar(self, nota):
        nota = nota + (self.avaliacao + self.total_avaliadores)
        self.total_avaliadores += 1
        self.avaliacao = round(nota / self.total_avaliadores, 2)

filme = Filme("1984", "Michael Radford", 1984)
filme.exibir_infos()
filme.avaliar(10.0)
filme.avaliar(8.0)
filme.avaliar(3.0)
filme.exibir_infos()


## Exercicio 02
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = [] # título e autor 

    def adicionar_livro (self, título, autor):
        self.livros.append({"título": título, "autor": autor})

    def remover_livros(self, título):
        for livro in self.livros:
            if livro["título"] == título:
                self.livros.remove(livro)
                print(f"Livro '{título}' removido")
                return

    print(f"Livro {'titulo'} não encontrado. ")

    def listar_livros(self):
        print(f"\n{self.nome}")
        if not self.livros:
            print("Biblioteca vazia. ")
        for livro in self.livros:
            print(f"- {livro['titulo']} ({livro['autor']})")

biblioteca = Biblioteca("Biblioteca Central")
biblioteca.adicionar_livro("Nagomi", "Ken Mogi")
biblioteca.adicionar_livro("Vagabond", "Takehiko Inoue")
biblioteca.listar_livros()
biblioteca.remover_livros("Nagomi")


## Exercicio 03
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_concluída(self):
        self.concluida = True

    def exibir(self):
        status = "[x]" if self.concluida else"[ ]"
        print(f"{status} {self.concluida}")
        return f"{status} {self.descricao}"

class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def listar_todas(self):
        for indice, tarefa in enumerate(self.tarefas):
            print(f"{indice + 1}, {tarefa.exibir()}")

    def listar_pendentes(self):
        for indice, tarefa in enumerate(self.tarefas):
            if not tarefa.concluida:
                print(f"{indice + 1}, {tarefa.exibir()}")

    def listar_concluídas(self):
        for indice, tarefa in enumerate(self.tarefas):
            if not tarefa.concluída:
                print(f"{indice + 1}, {tarefa.exibir}")

    def marcar_concluída(self, indice):
        if indice <= 0 or indice > len(self.tarefas):
            print("O indice informado está fora do intervalo de tarefas salvas")
            return

        self.tarefas[indice - 1].marcar_concluida()


lista = ListaTarefas()
lista.adicionar("Tarefa de exemplo")
lista.adicionar("Tarefa de programação")

print("Todas as tarefas: ")
lista.listar_todas()

lista.marcar_concluída(1)
lista.marcar_concluída(2)

print("\nTarefas pendentes:")
lista.listar_pendentes()

print("\nTarefas concluídas: ")
lista.listar_concluídas()
