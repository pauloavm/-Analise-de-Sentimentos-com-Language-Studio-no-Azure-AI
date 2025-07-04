# Projeto de Laboratório DIO: Análise de Fala e Linguagem com IA da Azure

Este repositório documenta a minha jornada de aprendizado e exploração das ferramentas de Inteligência Artificial da Microsoft Azure, especificamente o **Speech Studio** e o **Language Studio**. Este projeto foi desenvolvido como parte de um desafio de laboratório da [Digital Innovation One (DIO)](https://www.dio.me/).

## 📖 Descrição

O objetivo deste desafio é praticar e aprofundar os conhecimentos na utilização dos serviços cognitivos da Azure para análise de fala e de linguagem natural. A documentação a seguir serve como um guia dos passos realizados, insights adquiridos e um material de apoio para futuras consultas e implementações.

## 🛠️ Ferramentas Utilizadas

* **Microsoft Azure:** Plataforma de nuvem utilizada para provisionar os serviços de IA.
* **Azure Speech Studio:** Ferramenta para explorar funcionalidades de conversão de fala em texto, texto em fala, reconhecimento de locutor, entre outras.
* **Azure Language Studio:** Ferramenta para analisar texto, extrair informações, classificar sentimentos e entender a linguagem natural.
* **GitHub:** Plataforma utilizada para controle de versão e documentação do projeto.
* **Markdown:** Linguagem de marcação para formatação da documentação.

---

## 🚀 Minha Jornada de Exploração

A seguir, detalho os passos e aprendizados em cada uma das plataformas.

### **Parte 1: Azure Speech Studio (Análise de Fala)**

O Speech Studio é uma plataforma incrivelmente poderosa que permite testar e implementar funcionalidades de voz sem precisar escrever muito código inicialmente.

**1. Criação do Recurso Cognitivo:**
O primeiro passo foi acessar o portal da Azure e criar um novo recurso de "Serviços de Fala". Optei pelo nível de preço gratuito (Free F0) para este laboratório, o que é suficiente para explorar as principais funcionalidades.

**2. Exploração das Funcionalidades:**
* **Transcrição em Tempo Real (Real-time Speech-to-text):** Testei a transcrição de áudio do meu microfone diretamente na plataforma. A precisão da ferramenta em português foi impressionante.
    * **Insight:** A capacidade de identificar a pontuação automaticamente (vírgulas, pontos finais) torna o texto gerado muito mais legível e útil.
    * *Captura de Tela:*
        ![Exemplo de Transcrição em Tempo Real](imagens/resultado_transcricao.png) * **Análise de Pronúncia (Pronunciation Assessment):** Explorei como a ferramenta avalia a precisão e a fluência da fala em comparação com um texto de referência.
    * **Insight:** É uma ferramenta fantástica para aplicações de aprendizado de idiomas. Ela fornece feedback detalhado em nível de fonema.

**3. Conclusões sobre o Speech Studio:**
O Speech Studio desmistifica a tecnologia de voz. Com ele, é possível visualizar o potencial de aplicações como legendagem automática de vídeos, sistemas de atendimento ao cliente (URAs) inteligentes e ferramentas de acessibilidade para pessoas com deficiência auditiva.

---

### **Parte 2: Azure Language Studio (Análise de Linguagem)**

Similar ao Speech Studio, o Language Studio oferece uma interface visual para explorar as capacidades de processamento de linguagem natural (PLN) da Azure.

**1. Exploração das Funcionalidades:**
* **Análise de Sentimentos e Mineração de Opinião:** Utilizei esta funcionalidade para analisar avaliações de produtos. A ferramenta classifica o sentimento geral (positivo, negativo, neutro) e também identifica sentimentos relacionados a aspectos específicos do texto.
    * **Insight:** A mineração de opinião é mais poderosa que uma simples análise de sentimento, pois mostra *sobre o que* o cliente está falando bem ou mal (ex: "A bateria é ótima, mas a tela é ruim.").
    * *Captura de Tela:*
        ![Exemplo de Análise de Sentimento](imagens/language_studio_sentimentos.png) * **Extração de Frases-chave (Key Phrase Extraction):** Inseri um parágrafo de uma notícia e a ferramenta identificou os principais tópicos do texto.
    * **Insight:** Muito útil para indexação e resumo automático de grandes volumes de documentos, facilitando a busca por informações.

* **Reconhecimento de Entidades Nomeadas (Named Entity Recognition):** A ferramenta conseguiu identificar e categorizar nomes de pessoas, locais, organizações e datas em um texto.
    * **Insight:** Essencial para organizar dados não estruturados, como e-mails e documentos, e extrair informações valiosas para sistemas de CRM ou bases de conhecimento.

**2. Conclusões sobre o Language Studio:**
O Language Studio revela o poder de extrair valor de textos. As empresas podem usar essas ferramentas para entender o feedback dos clientes em escala, automatizar a classificação de documentos e criar assistentes virtuais mais inteligentes e contextuais.

---

## 👨‍💻 Exemplos de Código (SDK)

Para complementar a experiência nos Studios, explorei como utilizar estes serviços programaticamente usando o SDK da Azure para Python. Os scripts completos estão na pasta `/codigo`.

* **`analise_de_fala.py`**: Um script Python que utiliza o SDK de Fala da Azure para transcrever um arquivo de áudio (`.wav`) para texto.
* **`analise_de_texto.py`**: Um script Python que se conecta à API de Análise de Texto para realizar a análise de sentimento em uma frase.

## ✅ Conclusão Geral do Desafio

Este laboratório foi uma excelente oportunidade para ter contato prático com soluções de IA de ponta. Documentar o processo no GitHub solidificou o aprendizado e criou um material valioso para o meu portfólio. As ferramentas da Azure são acessíveis e poderosas, abrindo um leque de possibilidades para a criação de aplicações inteligentes.

## 🔗 Recursos Úteis

* [Documentação Oficial do Speech Studio](https://learn.microsoft.com/azure/ai-services/speech-service/speech-studio-overview)
* [Documentação Oficial do Language Studio](https://learn.microsoft.com/azure/ai-services/language-service/language-studio)
* [Guia de Markdown do GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

---

*Feito por Paulo Munhoz*
