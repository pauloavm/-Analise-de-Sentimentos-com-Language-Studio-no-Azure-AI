# Importa o SDK de Fala da Azure
import azure.cognitiveservices.speech as speechsdk
import os

# --- Configuração ---
# ATENÇÃO: Substitua pelos seus valores reais!
# Você pode encontrá-los no portal da Azure, na página do seu recurso de Fala.
SPEECH_KEY = "SUA_CHAVE_DE_API_AQUI"
SPEECH_REGION = "SUA_REGIAO_AQUI" # Ex: "eastus"

# --- Lógica Principal ---

def transcrever_de_arquivo(caminho_do_arquivo_wav):
    """
    Função que transcreve o áudio de um arquivo .wav para texto.
    """
    print("Iniciando o processo de reconhecimento de fala...")

    # Configura a conexão com o serviço de Fala da Azure
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    # Especifica o idioma do áudio
    speech_config.speech_recognition_language="pt-BR"

    # Configura a fonte do áudio (neste caso, um arquivo)
    audio_config = speechsdk.audio.AudioConfig(filename=caminho_do_arquivo_wav)

    # Cria o "reconhecedor" de fala com as configurações acima
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Inicia o reconhecimento. A função espera até que uma única declaração seja reconhecida.
    result = speech_recognizer.recognize_once_async().get()

    # --- Verificação do Resultado ---
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Reconhecido: \"{result.text}\"")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print(f"Não foi possível reconhecer a fala no arquivo: {result.no_match_details}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Reconhecimento cancelado: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Detalhes do erro: {cancellation_details.error_details}")
            print("Verifique se sua chave de API e região estão corretas e se o arquivo de áudio é válido.")

# --- Execução ---
if __name__ == '__main__':
    # Certifique-se de ter um arquivo de áudio .wav no mesmo diretório ou forneça o caminho completo.
    # Você pode gravar um áudio simples usando o Gravador de Voz do seu sistema operacional.
    arquivo_de_audio = "seu_audio.wav" 

    if not os.path.exists(arquivo_de_audio):
        print(f"Erro: Arquivo '{arquivo_de_audio}' não encontrado.")
        print("Por favor, coloque um arquivo .wav com este nome na mesma pasta do script ou ajuste o caminho.")
    else:
        transcrever_de_arquivo(arquivo_de_audio)
