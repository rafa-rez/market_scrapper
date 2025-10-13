# src/news_scraper.py
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from urllib.parse import urlparse, parse_qs

def _get_clean_url(google_url: str) -> str | None:
    """Extrai a URL real de um link de resultado de busca do Google."""
    parsed_url = urlparse(google_url)
    if parsed_url.path == '/url':
        query_params = parse_qs(parsed_url.query)
        return query_params.get('q', [None])[0]
    return None

def get_news_data(keywords, news_sites, max_news_per_site=3):
    """
    Raspa o CONTEÚDO COMPLETO de artigos do Google News com base em palavras-chave e sites.
    """
    results = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print(f"Buscando artigos em {len(news_sites)} site(s)...")

    for kw in keywords:
        for site_name, site_url in news_sites.items():
            try:
                google_search_url = f"https://www.google.com/search?q={kw}+site:{site_url}&tbm=nws&hl=pt-BR"
                
                response = requests.get(google_search_url, headers=headers, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, "html.parser")
                
                links = soup.select("a")
                count = 0
                for a in links:
                    if count >= max_news_per_site:
                        break
                    
                    raw_url = a.get('href')
                    if raw_url:
                        clean_url = _get_clean_url(raw_url)
                        if clean_url:
                            try:
                                print(f"  - Processando artigo de '{site_name}': {clean_url[:70]}...")
                                article = Article(clean_url)
                                article.download()
                                article.parse()
                                
                                if len(article.text) > 100: # Garante que o conteúdo foi extraído
                                    results.append({
                                        "site": site_name,
                                        "title": article.title,
                                        "content": article.text
                                    })
                                    count += 1
                            except Exception:
                                continue # Ignora artigos individuais que falham

            except requests.exceptions.RequestException as e:
                print(f"Aviso: Não foi possível buscar notícias de '{site_name}'. Erro: {e}")
                
    return results