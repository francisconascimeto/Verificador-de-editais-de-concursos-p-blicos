def analisar_proximidade(status):
    # Usar um dicionário para mapear pontos e mensagens melhora a manutenção
    etapas = {
        "anunciado": (2, "LONGE. O processo ainda é embrionário."),
        "solicitado": (3, "LONGE. O processo ainda é embrionário."),
        "autorizado": (5, "MÉDIO. O sinal ficou verde. Hora de intensificar!"),
        "comissão formada": (7, "PERTO. A estrutura do concurso está sendo montada."),
        "banca em definição": (8, "PERTO. A estrutura do concurso está sendo montada."),
        "banca definida": (9, "IMINENTE! O edital pode sair a qualquer momento."),
        "edital publicado": (10, "O edital já está na praça!")
    }

    status_limpo = status.lower().strip()

    if status_limpo in etapas:
        pontos, mensagem = etapas[status_limpo]
        print(f"\n--- Análise de Proximidade: {status_limpo.upper()} ---")
        print(f"Status: {mensagem}")
        print(f"Nível de prontidão sugerido: {pontos * 10}%")
    else:
        # Sugestão: listar as opções válidas dinamicamente
        opcoes = ", ".join(list(etapas.keys())[:3])
        print(f"Status desconhecido. Tente algo como: {opcoes}...")

# Teste do Programa
if __name__ == "__main__":
    print("=== Verificador de Editais ===")
    status_atual = input("Qual o Status do concurso? ")
    analisar_proximidade(status_atual)