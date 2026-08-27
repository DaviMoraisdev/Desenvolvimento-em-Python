import re

def validar_idade(idade: int) -> None:
    if not isinstance(idade, int):
        raise TypeError("A idade deve ser do tipo inteiro (int)")
    if idade < 0 :
        raise ValueError("A idade não pode começar negativa")
    if idade > 150:
        raise ValueError("A idade deve ser realista")


def validar_senha(senha: str) -> None:
    letra_pattern = r"[a-zA-Z]{1}"
    numero_pattern = r"\d"
    if not isinstance(senha, str):
        raise TypeError("A senha deve ser do tipo string(str)")
    if not senha:
        raise ValueError("A senha não pode estar vazia ")
    if len(senha) < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres")
    if not re.search(letra_pattern, senha) or not re.search(numero_pattern, senha):
        raise ValueError("A senha deve ter no mínimo 1 número e 1 letra")

try:
    validar_idade(151)
    validar_senha("avbcas123")
except Exception as error:
    print(f"Erro: {error}")