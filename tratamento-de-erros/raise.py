def definir_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    if idade > 140:
        raise ValueError("Idade deve ser realista")
    return idade

try:
    print(definir_idade(-5))
except ValueError as error:
    print(f"Erro: {error}")


"""class ContaBancaria:
    def __init__(self, titular, saldo):
        if not titular:
            raise ValueError("Titular não pode estar vazio")
        if saldo < 0:
            raise ValueError("Saldo não pode ser negativo")
        
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self.saldo += valor

# Uso
try:
    conta = ContaBancaria("", 1000)  # Erro
except ValueError as error:
    print(f"Erro: {error}")

try:
    conta = ContaBancaria("João", 1000)
    conta.sacar(2000)  # Erro
except ValueError as error:
    print(f"Erro: {error}")"""


class SaldoInsuficiente(Exception):
    def __init__(self, saldo_atual, valor_solicitado):
        self.saldo_atual = saldo_atual
        self.valor_solicitado = valor_solicitado

        mensagem = f"Saldo disponível: R$ {self.saldo_atual:.2f} solicitado: R$ {self.valor_solicitado:.2f}"
        super().__init__(mensagem)
class ContaBancaria:
    def __init__(self, valor):
        self.saldo = valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficiente(self.saldo, valor)

        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

try:
    conta = ContaBancaria(500)
    conta.sacar(500)
except SaldoInsuficiente as error:
    print(f"Erro: {error}")


class EmailInvalidoError(Exception):
    """Levantada quando um formato de e-mail não cumpre as regras de validação."""
    def __init__(self, email, motivo, codigo_erro):
        self.email = email
        self.motivo = motivo
        self.codigo_erro = codigo_erro  # Um identificador único para o tipo de erro
        
        super().__init__(f"O e-mail '{email}' é inválido. Motivo: {motivo} (Código: {codigo_erro})")

def validar_email(email):
    if not email or not email.strip():
        raise EmailInvalidoError(email, "O endereçp de e-mail não pode estar vazio.", "EMAIL_VAZIO")

    if "@" not in email:
        raise EmailInvalidoError(email, "O caractere '@' está ausente.", "SEM_ARROBA")

    partes = email.split("@")
    if len(partes) < 2 or "." not in partes[1]:
        raise EmailInvalidoError(email, "O domínio após o '@' é inválido ou não contém um ponto.", "DOMINIO_INVALIDDO")

    return email 

emails = ["valido@ex.com", "invalido", "sem.dominio@", ""]

for email in emails:
    try:
        validar_email(email)
        print(f"{email} -> Válido")
    except EmailInvalidoError as e:
        print(f"{email} -> Erro Capturado: {e}")

        if e.codigo_erro == "EMAIL VAZIO":
            print("Informe um e-mail")

