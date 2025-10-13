# main.py
from datetime import datetime

# Módulos do projeto
import config
from src.pdf_extractor import extract_all_pdfs_text
from src.news_scraper import get_news_data
from src.google_news_scraper import fetch_google_news_headlines # <--- NOVO
from src.ai_client import get_ai_analysis 

def main():
    """
    Função principal que orquestra a coleta, processamento e análise dos dados.
    """
    print("Iniciando processo de coleta e análise de dados...")

    # 1. Extração de textos de PDFs (sem truncamento)
    print(f"\n[1/4] Processando arquivos PDF da pasta '{config.PDF_FOLDER}'...")
    pdf_texts = extract_all_pdfs_text(config.PDF_FOLDER)
    pdf_summary = "\n\n".join([f"Arquivo {file}:\n{text}" for file, text in pdf_texts.items()])
    if not pdf_summary:
        pdf_summary = "Nenhum dado extraído de PDFs."
    print("Extração de PDFs concluída.")

    # 2. Coleta de manchetes do Google Notícias (substituindo Pytrends)
    print(f"\n[2/4] Coletando manchetes do Google Notícias para: {', '.join(config.KEYWORDS)}...")
    gn_headlines = fetch_google_news_headlines(config.KEYWORDS, max_headlines=15)
    if not gn_headlines:
        gn_summary = "Não foi possível coletar manchetes do Google Notícias."
    else:
        gn_summary = "\n".join([f"- {headline}" for headline in gn_headlines])
    print("Coleta de manchetes concluída.")

    # 3. Raspagem do conteúdo completo das notícias
    print("\n[3/4] Raspando conteúdo completo de artigos em sites configurados...")
    news_data = get_news_data(config.KEYWORDS, config.NEWS_SITES, max_news_per_site=3)
    news_summary = "\n\n".join([f"Fonte: {n['site']}\nTítulo: {n['title']}\nConteúdo:\n{n['content']}" for n in news_data])
    if not news_summary:
        news_summary = "Nenhum artigo relevante encontrado."
    print("Raspagem de artigos concluída.")

    # 4. Geração da análise com IA
    print("\n[4/4] Gerando análise com o modelo de linguagem...")
    final_prompt = config.USER_PROMPT_TEMPLATE.format(
        pdf_summary=pdf_summary,
        gn_summary=gn_summary, 
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