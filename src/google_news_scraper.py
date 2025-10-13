# src/google_news_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_google_news_headlines(keywords: list, max_headlines: int = 15) -> list:
    """
    Busca as manchetes mais recentes no Google Notícias para uma lista de palavras-chave.
    Isso substitui o Pytrends para medir o "interesse" atual do mercado.
    """
    results = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print("Buscando manchetes gerais no Google Notícias para análise de tendências...")
    
    query = " OR ".join(f'"{kw}"' for kw in keywords)
    
    try:
        url = f"https://news.google.com/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        articles = soup.find_all('article')
        for article in articles[:max_headlines]:
            title_tag = article.find('h3')
            if title_tag:
                title = title_tag.get_text().strip()
                results.append(title)
                
    except requests.exceptions.RequestException as e:
        print(f"Aviso: Não foi possível buscar manchetes no Google Notícias. Erro: {e}")
        
    return results