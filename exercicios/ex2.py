"""
jogo_forca.py
=============
Jogo da Forca em modo texto para terminal.

O programa sorteia uma palavra de uma lista pré-definida e permite ao
jogador adivinhar letras até completar a palavra ou esgotar o número
máximo de tentativas.

Módulos utilizados:
    random  — sorteio aleatório da palavra secreta a cada partida.
"""

import random


# ---------------------------------------------------------------------------
# Configurações globais
# ---------------------------------------------------------------------------

PALAVRAS: list[str] = [
    "PYTHON",
    "PROGRAMACAO",
    "ESTRUTURA",
    "VARIAVEL",
    "FUNCAO",
    "CONJUNTO",
    "LISTA",
    "DICIONARIO",
    "MODULO",
    "ALGORITMO",
]

MAX_TENTATIVAS: int = 6


# ---------------------------------------------------------------------------
# Funções principais
# ---------------------------------------------------------------------------

def inicializar_jogo() -> dict:
    """
    Prepara o estado inicial de uma nova partida.

    Sorteia aleatoriamente uma palavra da lista PALAVRAS usando
    ``random.choice``, que garante distribuição uniforme entre todos
    os elementos. Em seguida, constrói as estruturas de dados que
    representam o progresso do jogador.

    Returns:
        dict: Dicionário com as chaves:
            - ``palavra_secreta`` (str)  : palavra sorteada em maiúsculas.
            - ``palavra_oculta``  (list) : lista de ``"_"`` com um elemento
                                          por letra da palavra secreta;
                                          posições reveladas são substituídas
                                          pela letra correspondente.
            - ``letras_tentadas`` (set)  : conjunto das letras já enviadas
                                          pelo jogador (inicialmente vazio).
            - ``tentativas``      (int)  : contador regressivo de tentativas
                                          restantes (inicia em MAX_TENTATIVAS).
    """
    palavra = random.choice(PALAVRAS)

    return {
        "palavra_secreta": palavra,
        # Uma lista é usada aqui porque precisamos preservar a POSIÇÃO
        # de cada letra. Somente uma estrutura indexada permite escrever
        # palavra_oculta[i] = letra para revelar exatamente o caractere
        # correto sem alterar as demais posições.
        "palavra_oculta": ["_"] * len(palavra),

        # Um SET (conjunto) é usado para rastrear as letras já tentadas
        # pelos seguintes motivos:
        #   1. UNICIDADE automática: se o jogador digitar a mesma letra
        #      duas vezes, o set ignora a duplicata sem nenhum código extra.
        #   2. BUSCA em O(1): o operador `in` consulta a tabela de hash
        #      interna e responde em tempo constante, independentemente de
        #      quantas letras já foram tentadas. Em uma list, a mesma
        #      verificação seria O(n) — percorreria elemento por elemento.
        #   3. SEMÂNTICA clara: um set comunica explicitamente que cada
        #      letra aparece no máximo uma vez, o que é exatamente o
        #      invariante desejado para o histórico de tentativas.
        "letras_tentadas": set(),

        "tentativas": MAX_TENTATIVAS,
    }


def processar_tentativa(estado: dict, letra: str) -> str:
    """
    Processa uma única tentativa do jogador e atualiza o estado do jogo.

    Verifica, na ordem:
    1. Se a letra já foi tentada (consulta O(1) no set).
    2. Se a letra está na palavra secreta.
       - Sim → revela todas as ocorrências na lista ``palavra_oculta``.
       - Não → decrementa o contador de tentativas.

    Args:
        estado (dict): Dicionário de estado retornado por ``inicializar_jogo``
                       ou modificado por chamadas anteriores desta função.
                       É mutado diretamente: ``palavra_oculta``,
                       ``letras_tentadas`` e ``tentativas`` são atualizados
                       in-place.
        letra  (str):  Caractere único em maiúsculas a ser verificado.

    Returns:
        str: Mensagem de feedback a ser exibida ao jogador, descrevendo
             o resultado da tentativa (duplicata, acerto ou erro).
    """
    # Verificação de duplicata: O(1) graças à estrutura set.
    # Em uma list, seria necessário percorrer todos os elementos já tentados.
    if letra in estado["letras_tentadas"]:
        return f'  ↩  "{letra}" já foi tentada — nenhuma tentativa consumida.'

    # Registra a nova letra no set; duplicatas futuras serão bloqueadas
    # automaticamente pela própria natureza da estrutura.
    estado["letras_tentadas"].add(letra)

    if letra in estado["palavra_secreta"]:
        # enumerate fornece índice e valor simultaneamente, permitindo
        # atualizar exatamente as posições corretas na lista palavra_oculta.
        for i, caractere in enumerate(estado["palavra_secreta"]):
            if caractere == letra:
                estado["palavra_oculta"][i] = letra
        return f'  ✓  "{letra}" está na palavra!'
    else:
        estado["tentativas"] -= 1
        return (
            f'  ✗  "{letra}" não está na palavra. '
            f'Restam {estado["tentativas"]} tentativa(s).'
        )


# ---------------------------------------------------------------------------
# Fluxo principal
# ---------------------------------------------------------------------------

def main() -> None:
    """
    Controla o fluxo completo de uma partida do jogo da forca.

    Inicializa o estado via ``inicializar_jogo``, mantém o laço principal
    ``while`` enquanto houver tentativas e letras ocultas, valida cada
    entrada do usuário e exibe o feedback retornado por
    ``processar_tentativa``. Ao término do laço, determina e exibe o
    resultado final (vitória ou derrota).

    Returns:
        None
    """
    estado = inicializar_jogo()

    # O while usa condição composta com curto-circuito (and):
    #   - "tentativas > 0"           → evita derrota silenciosa.
    #   - '"_" in palavra_oculta'    → detecta vitória assim que a última
    #                                   letra é revelada, sem contador extra.
    # Qualquer uma das duas sendo False encerra o laço imediatamente.
    while estado["tentativas"] > 0 and "_" in estado["palavra_oculta"]:

        # --- exibir status da rodada ---
        print("\n" + "─" * 32)
        print("  " + " ".join(estado["palavra_oculta"]))

        # Barra de tentativas: barras cheias e vazias para feedback visual
        cheias = "❙" * estado["tentativas"]
        vazias = "░" * (MAX_TENTATIVAS - estado["tentativas"])
        print(f"  Tentativas: {cheias}{vazias}  ({estado['tentativas']} restante(s))")

        # sorted() exibe o set em ordem alfabética para facilitar a leitura;
        # sets não têm ordem definida, então a saída sem sort seria imprevisível.
        tentadas = ", ".join(sorted(estado["letras_tentadas"])) or "─"
        print(f"  Tentadas:   {tentadas}")

        # --- ler e validar entrada ---
        letra = input("\n  Letra: ").strip().upper()

        # Validação de entrada: deve ser exatamente um caractere alfabético.
        # continue retorna ao topo do while sem consumir tentativa.
        if len(letra) != 1 or not letra.isalpha():
            print("  ✗  Digite apenas uma letra (A–Z).")
            continue

        # --- processar e exibir feedback ---
        print(processar_tentativa(estado, letra))

    # --- resultado final ---
    # O while encerrou; precisamos distinguir os dois motivos possíveis:
    #   - Sem "_" na lista → jogador completou a palavra (vitória).
    #   - Com "_" na lista → tentativas chegaram a zero (derrota).
    print("\n" + "═" * 32)
    if "_" not in estado["palavra_oculta"]:
        print(f'  Parabéns! Você descobriu: {"".join(estado["palavra_oculta"])}')
    else:
        print(f'  Fim de jogo. A palavra era: {estado["palavra_secreta"]}')
    print("═" * 32 + "\n")


# Ponto de entrada: garante que main() só é chamada quando o script
# é executado diretamente, não quando importado como módulo.
if __name__ == "__main__":
    main()