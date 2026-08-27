import pytest
from validacao import validar_idade, validar_senha

def test_idade_valida():
    validar_idade(25)
    validar_idade(0)
    validar_idade(150)

def test_idade_tipo_incorreto():
    with pytest.raises(TypeError):
        validar_idade("25") # type: ignore

def test_idade_negativa():
    with pytest.raises(ValueError):
        validar_idade(-5)

def test_idade_muito_alta():
    with pytest.raises(ValueError):
        validar_idade(151)

def test_validar_senha():
    validar_senha("absbna123")
    validar_senha("123abcde")

def test_senha_incorreta():
    with pytest.raises(TypeError):
        validar_senha(123456) # type: ignore

def test_senha_vazia():
    with pytest.raises(ValueError):
        validar_senha("abc123")

def test_senha_curta():
    with pytest.raises(ValueError):
        validar_senha("abc123")

def test_senha_curta_sem_numero():
    with pytest.raises(ValueError):
        validar_senha("abc")

def test_senha_curta_sem_letra():
    with pytest.raises(ValueError):
        validar_senha("123")

def test_senha_sem_numero():
    with pytest.raises(ValueError):
        validar_senha("abcaasssd")