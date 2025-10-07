# Market Scrapper

Este projeto nasceu da ideia de **automatizar a coleta e a análise de inteligência de mercado**, unindo raspagem de dados, leitura de relatórios em PDF e modelos de linguagem avançados em uma única ferramenta.  

O objetivo é simples: transformar dados brutos em **insights**, ajudando a identificar tendências, movimentos do mercado e padrões de interesse em tempo real.

O diferencial está na **modularidade**, você pode conectar qualquer provedor de IA (OpenAI, Azure, Gemini, Claude ou Hugging Face) e personalizar fontes e prompts com facilidade, tudo a partir de um único arquivo de configuração.

---

## Principais Funcionalidades

- **Compatível com vários provedores de IA:**  
  Plugue o modelo de linguagem da sua preferência. Suporte nativo para:
  - Azure OpenAI  
  - OpenAI (API padrão)  
  - Google Gemini  
  - Anthropic Claude  
  - Hugging Face  

- **Extração automática de PDFs:**  
  Lê e processa relatórios em PDF de forma automática, prontos para análise.

- **Raspagem de notícias da web:**  
  Captura manchetes recentes de sites definidos e filtradas por palavras-chave.

- **Análise de tendências de busca:**  
  Integra-se ao Google Trends para medir o interesse público em diferentes temas ao longo do tempo.

- **Altamente configurável:**  
  Palavras-chave, sites, prompts e provedor de IA podem ser ajustados facilmente no `config.py`, sem tocar na lógica principal.

---

## Como Usar

### 1. Pré-requisitos

- Python 3.8 ou superior  
- Git instalado  
- Uma chave de API de um dos provedores suportados

---

### 2. Instalação

Clone o repositório:

```bash
git clone https://github.com/rafa-rez/market_scrapper.git
cd market_scrapper
```

Instale as dependências principais:

```bash
pip install pandas requests beautifulsoup4 pytrends python-dotenv pymupdf
```

E depois, instale **somente** a biblioteca do provedor de IA que for usar:

| Provedor         | Comando de Instalação             |
| ---------------- | --------------------------------- |
| Azure / OpenAI   | `pip install openai`              |
| Google Gemini    | `pip install google-generativeai` |
| Anthropic Claude | `pip install anthropic`           |
| Hugging Face     | `pip install huggingface_hub`     |

---

### 3. Configuração

#### a. Arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto e adicione **somente** as credenciais do provedor escolhido:

```env
# --- Azure OpenAI ---
AZURE_OPENAI_API_KEY="SUA_CHAVE_API"
AZURE_OPENAI_ENDPOINT="SEU_ENDPOINT"
AZURE_OPENAI_DEPLOYMENT="NOME_DO_SEU_DEPLOYMENT"

# --- OpenAI ---
OPENAI_API_KEY="sk-..."

# --- Google Gemini ---
GEMINI_API_KEY="..."

# --- Anthropic Claude ---
ANTHROPIC_API_KEY="..."

# --- Hugging Face ---
HUGGINGFACE_API_KEY="hf_..."
```

#### b. Configuração da análise (`config.py`)

Abra o `config.py` e ajuste os parâmetros principais:

- `AI_PROVIDER`: provedor de IA em uso (`"gemini"`, `"openai"`, etc)  
- `KEYWORDS`: lista de palavras-chave a serem analisadas  
- `NEWS_SITES`: sites de notícias a serem monitorados  
- `PDF_FOLDER`: pasta onde ficarão os arquivos PDF  
- `SYSTEM_PROMPT` e `USER_PROMPT_TEMPLATE`: instruções e contexto para o modelo de IA  

#### c. Adicione seus arquivos PDF

Crie a pasta definida em `PDF_FOLDER` (ex: `reports/`) e coloque seus relatórios `.pdf` nela.

---

### 4. Execução

Com tudo pronto, basta rodar:

```bash
python main.py
```

O script executa todas as etapas — coleta, processamento e análise — e gera um arquivo `.txt` com os resultados na raiz do projeto.

---

## 📁 Estrutura do Projeto

```
.
├── .env                    # Credenciais locais 
├── config.py               # Configuração principal do projeto
├── main.py                 # Ponto de entrada da aplicação
├── README.md               # Este mesmo arquivo
├── requirements.txt        # Dependências completas ( !! todas as bilbiotecas dos provedores estão incluídas !! )
└── src/                    # Código-fonte principal
    ├── __init__.py
    ├── ai_client.py        # Comunicação com diferentes APIs de IA
    ├── news_scraper.py     # Coleta de notícias da web
    └── pdf_extractor.py    # Extração de texto de PDFs
```

---

## 🧠 Futuras melhorias

- Dashboard interativo para visualização de insights  
- Suporte a bancos de dados (SQLite / Postgres)  
- Relatórios automáticos em Markdown ou PDF  
- Geração de resumos executivos  



Se curtiu o projeto, sinta-se à vontade para **contribuir, testar ou sugerir novas ideias**.  

---

<br>
<p align="center">
   <em>“Talk is cheap. Show me the code.”</em><br>
  — <strong>Linus Torvalds</strong>
</p>
