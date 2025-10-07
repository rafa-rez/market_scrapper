# config.py

# --- Configurações de Análise ---

# 1. Palavras-chave para a busca de dados.
KEYWORDS = ["BYD", "Veículo elétrico", "Carro por assinatura"]

# 2. Dicionário de sites para a raspagem de notícias.
#    Formato: "Nome do Site": "url_base_do_site.com"
NEWS_SITES = {
     "Quatro Rodas": "quatrorodas.abril.com.br",
    "Motor1": "motor1.com",
    "WM1 / Webmotors": "wm1.webmotors.com.br",
    "Autoesporte": "autoesporte.globo.com",
    "G1 Carros": "g1.globo.com/carros",
    "iCarros": "www.icarros.com.br"
}
# 3. Pasta onde os relatórios em PDF estão localizados.
PDF_FOLDER = "reports"

# --- Configurações da OpenAI ---

# 4. Instrução principal para a IA (define o "papel" dela).
SYSTEM_PROMPT = "Analise os dados a seguir e identifique tendências de consumo emergentes no mercado automotivo brasileiro, usando listas e bullet points:"

# 5. O prompt do usuário que será preenchido com os dados coletados.
#    Use as chaves {pdf_summary}, {trends_summary} e {news_summary} que serão substituídas pelos dados.
USER_PROMPT_TEMPLATE = """
Com base nos dados coletados a seguir, analise e identifique as principais tendências, desafios e oportunidades emergentes no setor automobílisto.

Estruture sua análise em bullet points, destacando os pontos mais importantes.

**Contexto Coletado:**

**1. Resumo de Relatórios (PDFs):**
{pdf_summary}

**2. Interesse de Busca (Google Trends):**
{trends_summary}

**3. Manchetes Recentes (Notícias):**
{news_summary}
"""

# --- Configurações de Saída ---

# 6. Prefixo para o nome do arquivo de resultado.
#    O resultado será salvo como: "analise_output_20251027_1530.txt"
OUTPUT_FILENAME_PREFIX = "analise_output"