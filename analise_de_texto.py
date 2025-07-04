# Importa o SDK de Análise de Texto (Linguagem) da Azure
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# --- Configuração ---
# ATENÇÃO: Substitua pelos seus valores reais!
# Você pode encontrá-los no portal da Azure, na página do seu recurso de Linguagem.
LANGUAGE_KEY = "SUA_CHAVE_DE_API_AQUI"
LANGUAGE_ENDPOINT = "SEU_ENDPOINT_AQUI" # Ex: "https://seurecurso.cognitiveservices.azure.com/"

# --- Lógica Principal ---

def autenticar_cliente():
    """Cria e autentica o cliente para acessar o serviço de linguagem."""
    ta_credential = AzureKeyCredential(LANGUAGE_KEY)
    text_analytics_client = TextAnalyticsClient(
            endpoint=LANGUAGE_ENDPOINT, 
            credential=ta_credential)
    return text_analytics_client

def analisar_sentimento(client, documentos):
    """
    Função que analisa o sentimento dos documentos de texto fornecidos.
    """
    try:
        print("Analisando o sentimento do texto...")
        response = client.analyze_sentiment(documents=documentos, language="pt-br")
        result = [doc for doc in response if not doc.is_error]

        # --- Exibição do Resultado ---
        for doc in result:
            print(f"\nDocumento: '{doc.id}'")
            print(f"Sentimento Geral: {doc.sentiment}")
            print(f"Pontuações de confiança: Positivo={doc.confidence_scores.positive:.2f}; " \
                  f"Neutro={doc.confidence_scores.neutral:.2f}; " \
                  f"Negativo={doc.confidence_scores.negative:.2f}")

    except Exception as err:
        print(f"Ocorreu um erro: {err}")
        print("Verifique se sua chave de API e endpoint estão corretos.")


# --- Execução ---
if __name__ == "__main__":
    client = autenticar_cliente()

    # Você pode testar com diferentes frases
    documentos_para_analise = [
        {"id": "1", "text": "O atendimento ao cliente foi horrível. Demorou muito e não resolveram meu problema."},
        {"id": "2", "text": "Amei o produto! A qualidade é excelente e a entrega foi super rápida."},
        {"id": "3", "text": "O preço do frete é razoável."}
    ]
    
    analisar_sentimento(client, documentos_para_analise)
