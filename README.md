# Market Scrapper


Bombardeados de nóticias, ficamos cegos para a verdade.

Este projeto nasceu da ideia de **automatizar a coleta e a análise de inteligência de mercado**, unindo raspagem de dados profundos, leitura de relatórios em PDF e modelos de linguagem avançados em uma única ferramenta. Tudo na tentantiva de ter insights aprimorados do mercado e me preparar para os movimentos da economia.

O objetivo é simples: transformar dados brutos e não estruturados em **insights acionáveis**, ajudando a identificar tendências, movimentos da concorrência e padrões de mercado em tempo real.

O diferencial está na **modularidade**: você pode conectar qualquer provedor de IA (OpenAI, Azure, Gemini, Claude ou Hugging Face) e personalizar fontes e prompts com facilidade, tudo a partir de um único arquivo de configuração.

---

## Principais Funcionalidades

- **Compatível com Múltiplos Provedores de IA:**
  Plugue o modelo de linguagem da sua preferência. Suporte nativo para:
  - Azure OpenAI
  - OpenAI (API padrão)
  - Google Gemini
  - Anthropic Claude
  - Hugging Face

- **Análise Profunda de PDFs:**
  Extrai o **conteúdo completo** de relatórios em formato PDF, permitindo que a IA analise os documentos na íntegra, sem truncamento.

- **Raspagem de Artigos Completos:**
  Não se limita a manchetes; o sistema acessa os links de notícias e extrai o **texto integral** dos artigos, fornecendo um contexto muito mais rico para a análise.

- **Monitoramento de Tendências via Notícias:**
  Utiliza o Google Notícias para capturar as manchetes mais recentes sobre as palavras-chave, servindo como um termômetro em tempo real do interesse e da cobertura da mídia sobre os temas.

- **Altamente Configurável:**
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
git clone [https://github.com/rafa-rez/market_scrapper.git](https://github.com/rafa-rez/market_scrapper.git)
cd market_scrapper
```

Instale as dependências principais:

```bash
pip install requirements.txt
```

E depois, instale **somente** a biblioteca do provedor de IA que for usar:

| Provedor         | Comando de Instalação             |
| ---------------- | --------------------------------- |
| Azure / OpenAI   | `pip install openai`              |
| Google Gemini    | `pip install google-generativeai` |
| Anthropic Claude | `pip install anthropic`           |
| Hugging Face     | `pip install huggingface-hub`     |

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

- `AI_PROVIDER`: provedor de IA em uso (`"gemini"`, `"openai"`, etc.)
- `KEYWORDS`: lista de palavras-chave a serem analisadas
- `NEWS_SITES`: sites de notícias para extração de artigos completos
- `PDF_FOLDER`: pasta onde ficarão os arquivos PDF para análise
- `SYSTEM_PROMPT` e `USER_PROMPT_TEMPLATE`: instruções e o template de contexto para o modelo de IA.

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
├── .env                     # Credenciais locais (não versionado)
├── config.py                # Configuração principal do projeto
├── main.py                  # Ponto de entrada da aplicação
├── README.md                # Este mesmo arquivo
└── src/                     # Código-fonte principal
    ├── __init__.py
    ├── ai_client.py           # Comunicação com diferentes APIs de IA
    ├── google_news_scraper.py # Captura de tendências via manchetes do Google Notícias
    ├── news_scraper.py        # Coleta do conteúdo completo de artigos
    └── pdf_extractor.py       # Extração de texto de PDFs
```

---

## Futuras Melhorias

- **Cache Inteligente:** Implementar um sistema de cache para evitar reprocessar PDFs e artigos já analisados.
- **Execução Assíncrona:** Utilizar `asyncio` para acelerar drasticamente a etapa de scraping de notícias.
- **CLI Interativa:** Adicionar argumentos de linha de comando (`argparse`) para passar palavras-chave e configurações sem editar o código.
- **Estratégia "Summarize-then-Synthesize":** Reduzir custos e aumentar a precisão ao primeiro resumir cada documento individualmente antes da análise final.
- **Relatórios Estruturados:** Gerar saídas em Markdown ou JSON em vez de `.txt`.

Se curtiu o projeto, sinta-se à vontade para **contribuir, testar ou sugerir novas ideias**.

---

<p align="center">
    <em>“Talk is cheap. Show me the code.”</em><br>
  — <strong>Linus Torvalds</strong>
</p>