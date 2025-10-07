# main.py
import pandas as pd
from datetime import datetime
import time

# Módulos do projeto
import config
from src.pdf_extractor import extract_all_pdfs_text
from src.news_scraper import get_news_data
from src.ai_client import get_ai_analysis 

# Bibliotecas de terceiros
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError


def fetch_interest_over_time(keywords):
    """
    Busca o interesse ao longo do tempo para palavras-chave no Google Trends.
    Se o limite de requisições for atingido, a etapa é pulada com um aviso.
    """
    pytrends = TrendReq(hl='pt-BR', tz=180)
    
    try:
        pytrends.build_payload(keywords, cat=0, timeframe='today 3-m', geo='BR')
        data = pytrends.interest_over_time()
        if not data.empty and 'isPartial' in data.columns:
            data = data.drop(columns=['isPartial'])
        return data
    except TooManyRequestsError:
        # Se o Google bloquear, exibe um aviso e continua a execução sem os dados do Trends.
        print("Aviso: Limite de requisições ao Google Trends atingido. Esta etapa será ignorada.")
        return pd.DataFrame() # Retorna um DataFrame vazio para não quebrar o resto do script
    except Exception as e:
        print(f"Erro inesperado ao consultar o Google Trends: {e}")
        return pd.DataFrame()


def main():
    """
    Função principal que orquestra a coleta, processamento e análise dos dados.
    """
    print("Iniciando processo de coleta e análise de dados...")

    # 1. Extração de textos de PDFs
    print(f"\n[1/4] Processando arquivos PDF da pasta '{config.PDF_FOLDER}'...")
    pdf_texts = extract_all_pdfs_text(config.PDF_FOLDER)
    pdf_summary = "\n\n".join([f"Arquivo {file}:\n{text[:1500]}..." for file, text in pdf_texts.items()])
    if not pdf_summary:
        pdf_summary = "Nenhum dado extraído de PDFs."
    print("Extração de PDFs concluída.")

    # 2. Coleta de dados do Google Trends
    print(f"\n[2/4] Coletando dados do Google Trends para: {', '.join(config.KEYWORDS)}...")
    trends_data = fetch_interest_over_time(config.KEYWORDS)
    if trends_data.empty:
        trends_summary = "Não foi possível coletar os dados do Google Trends."
    else:
        trends_summary = trends_data.tail().to_string()
    print("Coleta do Google Trends concluída.")

    # 3. Raspagem de notícias
    print("\n[3/4] Raspando notícias de sites configurados...")
    news_data = get_news_data(config.KEYWORDS, config.NEWS_SITES, max_news_per_site=5)
    news_summary = "\n".join([f"- {n['title']} ({n['site']})" for n in news_data])
    if not news_summary:
        news_summary = "Nenhuma notícia relevante encontrada."
    print("Raspagem de notícias concluída.")

    # 4. Geração da análise com IA
    print("\n[4/4] Gerando análise com o modelo de linguagem...")
    final_prompt = config.USER_PROMPT_TEMPLATE.format(
        pdf_summary=pdf_summary,
        trends_summary=trends_summary,
        news_summary=news_summary
    )
    
    analysis_result = get_ai_analysis(config.SYSTEM_PROMPT, final_prompt)

    # 5. Salvamento do resultado
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = f"{config.OUTPUT_FILENAME_PREFIX}_{timestamp}.txt"
    
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(analysis_result)
        print(f"\nAnálise concluída com sucesso! Resultado salvo em: {output_file}")
    except IOError as e:
        print(f"\nErro ao salvar o arquivo de resultado: {e}")


if __name__ == "__main__":
    main()