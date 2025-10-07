# config.py
import os

# --- Configurações de Análise ---
KEYWORDS = ["Inteligência Artificial", "Machine Learning", "Big Data"]
NEWS_SITES = {"TecMundo": "tecmundo.com.br", "Canaltech": "canaltech.com.br"}
PDF_FOLDER = "reports"

# --- Configurações da IA ---

# Escolha o provedor de IA. Opções: "azure", "openai", "gemini", "claude", "huggingface"
AI_PROVIDER = "azure" 

# Modelos e credenciais para cada provedor (puxados do .env)
AI_CONFIG = {
    "azure": {
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "deployment": os.getenv("AZURE_OPENAI_DEPLOYMENT")
    },
    "openai": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "gpt-4o"  # Ou "gpt-3.5-turbo"
    },
    "gemini": {
        "api_key": os.getenv("GEMINI_API_KEY"),
        "model": "gemini-1.5-flash"
    },
    "claude": {
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "model": "claude-3-haiku-20240307" # Modelo mais rápido e econômico
    },
    "huggingface": {
        "api_key": os.getenv("HUGGINGFACE_API_KEY"),
        "model": "mistralai/Mistral-7B-Instruct-v0.2" # Exemplo de modelo
    }
}

# --- Configurações de Prompt ---
SYSTEM_PROMPT = "Você é um analista de mercado e tecnologia, especialista em identificar tendências emergentes e padrões de dados."
USER_PROMPT_TEMPLATE = """
Com base nos dados coletados a seguir, analise e identifique as principais tendências, desafios e oportunidades emergentes.

**Contexto Coletado:**
1. Resumo de Relatórios (PDFs): {pdf_summary}
2. Interesse de Busca (Google Trends): {trends_summary}
3. Manchetes Recentes (Notícias): {news_summary}
"""

# --- Configurações de Saída ---
OUTPUT_FILENAME_PREFIX = "analise_de_tendencias"