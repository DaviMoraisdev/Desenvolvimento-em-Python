from datetime import datetime

class Convidado:
    """Representa um convidado individual do evento"""

    def __init__(self, nome: str, codigo: str = "", status: str = "Pendente", entrada_em: str = "") -> None:
        self._nome = nome
        self._codigo = codigo if codigo else self.gerar_codigo(nome)
        self._status = status
        self._entrada_em = entrada_em

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def status(self) -> str:
        return self._status

    @property
    def entrada_em(self) -> str:
        return self._entrada_em

    @staticmethod
    def gerar_codigo(nome_completo: str) -> str:
        """Gera o código único: 3 primeiras letras + 2 últimas do nome sem espaços """
        nome_limpo = nome_completo.replace(" ", "")
        if len(nome_limpo) < 5:
            return nome_limpo.upper()
        return (nome_limpo[:3] + nome_limpo[-2:]).upper()

    def confirmar_entrada(self) -> None:
        """Altera o status para confirmado e registra o timestamp atual no formato DD/MM/AAAA HH:MM:ss."""
        self._status = "Confirmado"
        self._entrada_em = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def definir_pendente(self) -> None:
        """Garante ou reverte o status do convidado para Pendente"""
        self._status = "Pendente"
        self._entrada_em = ""

import csv
import os

class GerenciadorPortaria:
    """Gerencia a lista de convidados, leitura, escrita e buscas na base de dados"""

    def __init__(self, caminho_csv: str = "lista_eventos.csv") -> None:
        self.caminho_csv = caminho_csv
        self.convidados: list[Convidado] = []

    def importar_de_txt(self, caminho_txt: str) -> bool:
        """Lê um TXT de nomes, gera objetos Convidado e exporta para o formato CSV inicial"""
        if os.path.exists(self.caminho_csv):
            resposta = input("O arquivo CSV já existe. Deseja sobrescrevê-lo? (S/N): ").strip().upper()
            if resposta != "S":
                return self.carregar_csv()

        try:
            with open(caminho_txt, "r", encoding="utf-8") as txt:
                nomes = [linha.strip() for linha in txt if linha.strip()]

            self.convidados = [Convidado(nome) for nome in nomes]
            self.salvar_csv()
            return True
        except FileNotFoundError:
            return False

    def carregar_csv(self) -> bool:
        """Carrrega a base de dados do CSV para a memória do programa."""
        if not os.path.exists(self.caminho_csv):
            return False
        try:
            self.convidados.clear()
            with open(self.caminho_csv, "r", encoding="utf-8") as f:
                leitor = csv.DictReader(f)
                for linha in leitor:
                    self.convidados.append(
                        Convidado(linha["nome"], linha["codigo"], linha["status"], linha["entrada_em"])
                    )
            return True
        except Exception:
            return False

    def salvar_csv(self) -> None:
        """Escreve o estado atual dos convidados da memória direto no arquivo CSV. """
        with open(self.caminho_csv, "w", newline="", encoding="utf-8") as f:
            campos = ["nome", "codigo", "status", "entrada_em"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for c in self.convidados:
                escritor.writerow({
                    "nome": c.nome,
                    "codigo": c.codigo,
                    "status": c.status,
                    "entrada_em": c.entrada_em
                })

    def buscar_por_termo(self, termo: str) -> list[Convidado]:
        """Procura correspondências exatas pelo codigo ou parciais pelo nome. """
        termo_formatado = termo.strip().upper()
        resultados = []
        for c in self.convidados:
            if c.codigo == termo_formatado or termo_formatado in c.nome.upper():
                resultados.append(c)
        return resultados
