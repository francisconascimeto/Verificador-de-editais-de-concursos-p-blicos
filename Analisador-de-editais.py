import requests

# url base do concurso(exemplo hipotético)
url = "https://api.concursos.exemplo.com/v1/abertos"

# headers para autenticação(se necessário)
headers = {
    "authorization":"BEARER SUA_CHAVE_API"
    "Content-Type":"application/json"
}

try:
    # Realiza a requisição GET
    response = requests.get(url, headers=headers)

#Verifica se a requisição foi bem sucedida(Status 200)
if response.status_code == 200:
    dados = response.json()
# Processar os dados(ex:Printar concursos)
for concursos in dados['concursos']:
    print(f"Concurso: {concurso['nome']} Banca: {concurso['banca'}")
else:
    print(f"Erro na API {response.status_code}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

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
