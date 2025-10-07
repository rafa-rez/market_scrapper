# news_scraper.py
import requests
from bs4 import BeautifulSoup

def get_news_data(keywords, news_sites, max_news_per_site=5):
    """
    Raspa manchetes do Google News com base em palavras-chave e uma lista de sites.

    Args:
        keywords (list): Lista de palavras-chave para buscar.
        news_sites (dict): Dicionário com nomes e URLs dos sites.
        max_news_per_site (int): Número máximo de notícias para coletar por site.

    Returns:
        list: Uma lista de dicionários contendo as notícias encontradas.
    """
    results = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    total_sites = len(news_sites)
    print(f"Buscando notícias em {total_sites} site(s) para {len(keywords)} palavra(s)-chave...")

    for kw in keywords:
        for site_name, site_url in news_sites.items():
            try:
                # Usa o Google News como intermediário para buscar no site específico
                url = f"https://www.google.com/search?q={kw}+site:{site_url}&tbm=nws&hl=pt-BR"
                
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()  # Lança um erro para status HTTP ruins (4xx ou 5xx)
                
                soup = BeautifulSoup(response.text, "html.parser")
                
                links = soup.select("a") # Seleciona todos os links na página de resultados
                count = 0
                for a in links:
                    title_element = a.find('h3') # Títulos de notícias no Google geralmente estão em H3
                    if title_element:
                        title = title_element.get_text().strip()
                        if len(title) > 20: # Filtro simples para evitar links de navegação
                            results.append({
                                "site": site_name,
                                "title": title,
                                "content": f"Manchete sobre '{kw}'"
                            })
                            count += 1
                            if count >= max_news_per_site:
                                break
                                
            except requests.exceptions.RequestException as e:
                print(f"Aviso: Não foi possível buscar notícias de '{site_name}'. Erro: {e}")
            except Exception as e:
                print(f"Aviso: Ocorreu um erro inesperado ao processar '{site_name}': {e}")
                
    return results