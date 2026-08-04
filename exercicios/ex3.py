"""
Sistema de gerenciamento de notas - estrutura base de dados.

Requisito de armazenamento:
- Usar lista de dicionários.
- Cada dicionário deve conter, no mínimo:
  - "nome": string
  - "notas": lista de float
"""

# Lista principal que armazenará todos os estudantes cadastrados.
estudantes = [
    {"nome": "Ana Silva", "notas": [8.5, 7.0, 9.2]},
    {"nome": "Bruno Costa", "notas": [6.0, 5.5, 7.0]},
    {"nome": "Carla Souza", "notas": [9.0, 8.8, 9.5]},
]

# Exemplo de novo cadastro seguindo a mesma estrutura.
novo_estudante = {"nome": "Davi Morais", "notas": [7.5, 8.0, 6.5]}
estudantes.append(novo_estudante)

def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.

    Args:
        notas (list[float]): Lista com as notas do estudante.

    Returns:
        float: Valor da média.

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")

    return sum(notas) / len(notas)


def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica situação de aprovação com base na média mínima exigida.

    Args:
        media (float): Média final do estudante.
        media_minima (float, optional): Nota mínima para aprovação. Padrão: 7.0.

    Returns:
        str: 'Aprovado' se media >= media_minima, senão 'Reprovado'.
    """
    if media >= media_minima:
        return "Aprovado"
    return "Reprovado"


def gerar_relatorio(alunos):
    """
    Exibe no terminal um relatório com nome, média e situação de cada estudante.

    Args:
        alunos (list[dict]): Lista de estudantes no formato
            {"nome": str, "notas": list[float]}.
    """
    print("RELATÓRIO DE DESEMPENHO ACADÊMICO")
    print("-" * 45)

    for aluno in alunos:
        nome = aluno["nome"]
        notas = aluno["notas"]
        media = calcular_media(notas)
        situacao = verificar_aprovacao(media)

        print(f"Nome: {nome}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("-" * 45)
