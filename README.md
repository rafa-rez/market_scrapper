# Market Scrapper

Este projeto é uma ferramenta automatizada para coleta e análise de tendências de mercado usando raspagem de dados, APIs e um modelo de linguagem da OpenAI. A ferramenta coleta informações de PDFs locais, notícias da web e dados do Google Trends para gerar um relatório analítico sobre um determinado setor.

O projeto foi projetado para ser facilmente configurável para qualquer área de mercado, bastando alterar um único arquivo de configuração.

## Funcionalidades

-   **Extração de Dados de PDFs:** Processa todos os arquivos `.pdf` em uma pasta designada, extraindo seu conteúdo de texto.
-   **Raspagem de Notícias:** Coleta as manchetes mais recentes de uma lista configurável de sites de notícias com base em palavras-chave.
-   **Análise de Tendências de Busca:** Utiliza a API do Google Trends para buscar o interesse ao longo do tempo para as palavras-chave definidas.
-   **Análise com Inteligência Artificial:** Consolida todos os dados coletados e os envia para a API da Azure OpenAI para gerar um resumo analítico e identificar tendências.
-   **Altamente Configurável:** Todas as fontes de dados, palavras-chave e prompts da IA podem ser facilmente ajustados no arquivo `config.py`.

## Como Usar

### 1. Pré-requisitos

-   Python 3.8 ou superior
-   Uma chave de API da Azure OpenAI

### 2. Instalação

Clone o repositório e instale as dependências:

```bash
git clone [https://github.com/rafa-rez/market_scrapper.git]
cd market_scrapper
pip install -r requirements.txt
```

### 3. Configuração

a. **Variáveis de Ambiente:**
Crie um arquivo chamado `.env` na raiz do projeto e adicione suas credenciais da Azure OpenAI:

```
AZURE_OPENAI_API_KEY="SUA_CHAVE_API"
AZURE_OPENAI_ENDPOINT="SEU_ENDPOINT"
AZURE_OPENAI_DEPLOYMENT="NOME_DO_SEU_DEPLOYMENT"
```

b. **Configuração da Análise:**
Abra o arquivo `config.py` e personalize os seguintes campos de acordo com o seu objetivo:

-   `KEYWORDS`: Lista de palavras-chave para a análise.
-   `NEWS_SITES`: Dicionário com os sites de onde as notícias serão extraídas.
-   `PDF_FOLDER`: Nome da pasta onde você colocará os PDFs para análise.
-   `SYSTEM_PROMPT` e `USER_PROMPT_TEMPLATE`: O cérebro da IA. Adapte-os para definir o tom e o formato da análise desejada.
-   `OUTPUT_FILENAME_PREFIX`: Prefixo do arquivo de texto que será salvo com o resultado.

c. **Adicionar PDFs:**
Crie a pasta definida em `PDF_FOLDER` (por exemplo, `reports`) e coloque seus arquivos `.pdf` dentro dela.

### 4. Execução

Para iniciar a análise, basta executar o script principal:

```bash
python main.py
```

Ao final do processo, um arquivo `.txt` com a análise completa será salvo na raiz do projeto.

## Estrutura do Projeto

```
.
├── config.py               # Arquivo de configuração principal
├── main.py                 # Orquestrador do processo
├── news_scraper.py         # Módulo para raspagem de notícias
├── openai_client.py        # Módulo para interação com a API da OpenAI
├── pdf_extractor.py        # Módulo para extração de texto de PDFs
├── requirements.txt        # Lista de dependências
├── .env                    # Arquivo para credenciais (não versionar)
└── reports/                # Pasta de exemplo para os PDFs
    └── relatorio_exemplo.pdf
```