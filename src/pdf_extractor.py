# pdf_extractor.py
import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extrai o conteúdo de texto de um único arquivo PDF.
    """
    try:
        with fitz.open(pdf_path) as doc:
            text = "".join(page.get_text("text") for page in doc)
        return text.strip()
    except Exception as e:
        print(f"Erro ao ler o arquivo PDF {pdf_path}: {e}")
        return ""

def extract_all_pdfs_text(folder_path: str) -> dict:
    """
    Extrai texto de todos os arquivos PDF dentro de uma pasta especificada.
    Retorna um dicionário com o nome do arquivo como chave e o texto como valor.
    """
    all_texts = {}
    if not os.path.isdir(folder_path):
        print(f"Aviso: O diretório '{folder_path}' não foi encontrado.")
        return all_texts

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            print(f"  - Extraindo texto de: {filename}")
            text = extract_text_from_pdf(path)
            if text:
                all_texts[filename] = text
    return all_texts