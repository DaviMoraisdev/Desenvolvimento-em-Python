import pytest
from portaria import Convidado, GerenciadorPortaria

# --- FIXTURES (Preparação do ambiente de testes) ---

@pytest.fixture
def convidado_pendente():
    """Retorna uma instância limpa de Convidado para testes."""
    return Convidado("Ana Maria")

@pytest.fixture
def gerenciador_com_dados():
    """Retorna um gerenciador pré-populado na memória para testar buscas."""
    gerenciador = GerenciadorPortaria("test_lista.csv")
    gerenciador.convidados = [
        Convidado("Felipe Silva"),
        Convidado("Ana Maria")
    ]
    return gerenciador

# --- TESTES DA CLASSE CONVIDADO ---

def test_geracao_codigo_padrao() -> None:
    """Garante que a regra de 3 primeiras letras + 2 últimas funciona em maiúsculas."""
    codigo = Convidado.gerar_codigo("Felipe Silva")
    assert codigo == "FELVA"

def test_geracao_codigo_nome_unico() -> None:
    """Testa geração de código em strings contínuas sem sobrenome."""
    codigo = Convidado.gerar_codigo("Arthur")
    assert codigo == "ARTUR"

def test_confirmar_entrada(convidado_pendente: Convidado) -> None:
    """Verifica alteração de status e criação automática do timestamp de entrada."""
    assert convidado_pendente.status == "Pendente"
    assert convidado_pendente.entrada_em == ""

    convidado_pendente.confirmar_entrada()
    assert convidado_pendente.status == "Confirmado"
    assert convidado_pendente.entrada_em != ""

# --- TESTES DA CLASSE GERENCIADORPORTARIA ---

def test_buscar_por_codigo_exato(gerenciador_com_dados: GerenciadorPortaria) -> None:
    """Garante a localização de um convidado pelo código uppercase."""
    resultados = gerenciador_com_dados.buscar_por_termo("FELVA")
    assert len(resultados) == 1
    assert resultados[0].nome == "Felipe Silva"

def test_buscar_por_nome_parcial_case_insensitive(gerenciador_com_dados: GerenciadorPortaria) -> None:
    """Testa a tolerância a termos minúsculos e buscas parciais."""
    resultados = gerenciador_com_dados.buscar_por_termo("maria")
    assert len(resultados) == 1
    assert resultados[0].codigo == "ANAIA"