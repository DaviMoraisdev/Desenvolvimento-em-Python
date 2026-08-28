from portaria import GerenciadorPortaria, Convidado
from pathlib import Path

def processar_comando_administrativo(comando: str, gerenciador: GerenciadorPortaria) -> None:
    """Processa comandos globais da portaria (total, confirmados, pendentes, pendente <nome>)."""
    comando = comando.strip().lower()
    total_cadastrados = len(gerenciador.convidados)

    if comando == "total":
        confirmados = sum(1 for c in gerenciador.convidados if c.status == "Confirmado")
        pct = (confirmados / total_cadastrados * 100) if total_cadastrados > 0 else 0
        print(f"\n📊 [RELATÓRIO]: Cadastrados: {total_cadastrados} | Presenças: {confirmados} | Ocupação: {pct:.1f}%")

    elif comando == "confirmados":
        print("\n✅ --- LISTA DE PRESENTES ---")
        for c in gerenciador.convidados:
            if c.status == "Confirmado":
                print(f"- {c.nome} [{c.codigo}] às {c.entrada_em}")

    elif comando == "pendentes":
        print("\n⏳ --- LISTA DE ESPERA/PENDENTES ---")
        for c in gerenciador.convidados:
            if c.status == "Pendente":
                print(f"- {c.nome} [{c.codigo}]")

    elif comando.startswith("pendente "):
        busca = comando.replace("pendente ", "")
        encontrados = gerenciador.buscar_por_termo(busca)
        # Reutilizar lógica de seleção se houver homônimos para remover o check-in
        if encontrados:
            selecionado = selecionar_convidado(encontrados)
            if selecionado:
                selecionado.definir_pendente()
                gerenciador.salvar_csv()
                print(f"🔄 {selecionado.nome} voltou para o status PENDENTE.")
        else:
            print("❌ Convidado não encontrado para remoção de confirmação.")

def selecionar_convidado(lista: list[Convidado]) -> Convidado | None:
    """Caso haja mais de um resultado, força a escolha via índice numérico."""
    if len(lista) == 1:
        return lista[0]

    print("\n⚠️ Múltiplos convidados encontrados:")
    for idx, c in enumerate(lista, 1):
        print(f"{idx}. {c.nome} [{c.codigo}] - Status: {c.status}")

    try:
        escolha = int(input("Digite o número do convidado correto: "))
        if 1 <= escolha <= len(lista):
            return lista[escolha - 1]
    except ValueError:
        pass
    print("❌ Opção inválida.")
    return None

if __name__ == "__main__":
    diretorio_projeto = Path(__file__).resolve().parent
    gerenciador = GerenciadorPortaria(str(diretorio_projeto / "lista_eventos.csv"))

    # Tenta carregar banco existente, senão importa do txt inicial
    if not gerenciador.carregar_csv():
        print("Base CSV não encontrada. Tentando importar dados de 'convidados.txt'...")
        if not gerenciador.importar_de_txt(str(diretorio_projeto / "convidados.txt")):
            print("❌ Erro fatal: Arquivos 'lista_eventos.csv' e 'convidados.txt' ausentes.")
            exit(1)

    print("\n🚀 SISTEMA DE PORTARIA ONEBITCODE INICIALIZADO COM SUCESSO!")

    while True:
        entrada = input("\nPortaria > Informe Nome, Código ou Comando: ").strip()

        if not entrada:
            continue
        if entrada.lower() == "sair":
            print("Encerrando portaria... Dados salvos com segurança.")
            break

        # Verifica se é um comando administrativo
        if entrada.lower() in ["total", "confirmados", "pendentes"] or entrada.lower().startswith("pendente "):
            processar_comando_administrativo(entrada, gerenciador)
            continue

        # Executa busca padrão por convidado
        resultados = gerenciador.buscar_por_termo(entrada)

        if not resultados:
            print("❌ [ALERTA]: Convidado não localizado na lista oficial.")
            continue

        convidado = selecionar_convidado(resultados)
        if convidado:
            if convidado.status == "Confirmado":
                print(f"⚠️ [ATENÇÃO]: {convidado.nome} JÁ ENTROU no evento em {convidado.entrada_em}!")
            else:
                convidado.confirmar_entrada()
                gerenciador.salvar_csv()
                print(f"🎉 [SUCESSO]: Check-in Confirmado! Seja bem-vindo(a), {convidado.nome}!")
